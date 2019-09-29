import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        BACKEND_URL: 'http://backendhackers.scapp.io/',
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
            selectedCategories: [],
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
        updateCategorySelection(state, payload) {
            state.surprise.selectedCategories = payload.categories;
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
            const data = JSON.stringify({
                locationId: context.state.surprise.startLocation.id,
                date: context.state.surprise.startDate,
                categories: context.state.surprise.selectedCategories
            });
            const result = await fetch(context.state.BACKEND_URL + 'surprise', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: data
            });
            const response = await result.json();
            console.log(response);
            this.saveToStore(response);
        },
        saveToStore(result) {
            this.updateSurprises(this.state, result);

            const surprise = result[0];
            this.updateLocation(this.state, {startLocation: {id: surprise.originId, name: surprise.startLocation}});
            this.parseAndSaveTime(surprise);
            const price = surprise.price / 10;
            this.updatePrice(this.state, price);
        },
        parseAndSaveTime(surprise) {
            let startDateTime = surprise.firstLeg.startTime;
            startDateTime = new Date(startDateTime);
            let date = startDateTime.getDay() + "." + startDateTime.getMonth() + "." + startDateTime.getFullYear();
            let startTime = startDateTime.getHours() + ":" + startDateTime.getMinutes();
            let endDateTime = surprise.secondLeg.endTime;
            endDateTime = new Date(endDateTime);
            let endTime = endDateTime.getHours() + ":" + endDateTime.getMinutes();
            this.updateDate(this.state, date);
            this.updateStartTime(this.state, startTime);
            this.updateEndTime(this.state, endTime);
        }
    }
})
