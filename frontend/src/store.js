import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        wizard: {
            currentStep: 0
        },
        surprise: {
            startDate: null,
            startTime: null,
            endTime: null,
            startLocation: {
                id: null,
                name: null
            },
            categories: [],
            price: null
        },
        surprises: []
    },
    mutations: {
        updateLocation(state, payload) {
            state.surprise.startLocation.id = payload.startLocation.id;
            state.surprise.startLocation.name = payload.startLocation.name;
        },
        updateDate(state, payload) {
            state.surprise.startDate = payload.startDate;
        },
        updateCategories(state, payload) {
            state.surprise.categories = payload.categories;
        },
        updateStartTime(state, payload) {
            state.surprise.startTime = payload.startTime;
        },
        updateEndTime(state, payload) {
            state.surprise.endTime = payload.endTime;
        },
        updatePrice(state, payload) {
            state.surprise.price = payload.price;
        },
        updateSurprises(state, payload) {
            state.surprises = payload
        }
    },
    actions: {}
})
