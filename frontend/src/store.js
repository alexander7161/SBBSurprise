import Vue from 'vue'
import Vuex from 'vuex'

import moment from 'moment'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        BACKEND_URL: 'http://backendhackers.scapp.io/',
        wizard: {
            currentStep: 0,
            startLocation: {
                id: null,
                name: null
            },
            startDate: null,
            categories: [],
            selectedCategories: [],
            loading: false
        },
        surprise: {
            startTime: null,
            endTime: null,
            price: null
        },
        offers: []
    },
    getters: {
        getOffer: (state) => (index) => {
            if (index >= state.offers) {
                // abort
            }
            const selectedSurprise = state.offers[index];
            const beginning = moment(selectedSurprise.firstLeg.startTime);
            const end = moment(selectedSurprise.secondLeg.endTime);
            console.log(selectedSurprise);
            return {
                startDate: beginning.format('DD-MM-YYYY'),
                startTime: beginning.format('HH:mm'),
                endTime: end.format('HH:mm'),
                price: selectedSurprise.price / 100.0
            };
        }
    },
    mutations: {
        updateLocation(state, payload) {
            state.wizard.startLocation = payload.startLocation;
        },
        updateDate(state, payload) {
            state.wizard.startDate = payload.startDate;
        },
        updateCategories(state, payload) {
            state.wizard.categories = payload.categories;
        },
        updateCategorySelection(state, payload) {
            state.wizard.selectedCategories = payload.categories;
        },
        updateOffersData(state, payload) {
            state.offers = payload;
        },
        setLoading(state, loading) {
            state.wizard.loading = loading;
        },
        setSurprise(state, surpriseData) {
            state.surprise = surpriseData;
        }
    },
    actions: {
        async getCategories(context) {
            const result = await fetch(context.state.BACKEND_URL + 'categories', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            if (result.ok) {
                context.commit('updateCategories', {categories: await result.json()})
            } else {
                console.log(result);
                console.error('no result')
            }
        },
        async postSurprise(context) {
            context.commit('setLoading', true);
            const result = await fetch(context.state.BACKEND_URL + 'surprise', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    locationId: context.state.wizard.startLocation.id,
                    date: context.state.wizard.startDate,
                    categories: context.state.wizard.selectedCategories
                })
            });
            const response = await result.json();
            context.commit('updateOffersData', response);
            console.log(context.state.offers);
            console.log(context.getters.getOffer(0));
            context.commit('setSurprise', context.getters.getOffer(0));
            context.commit('setLoading', false);
        }
    }
})
