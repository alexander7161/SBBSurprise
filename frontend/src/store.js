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
      startLocation: {
        id: null,
        name: null
      },
      categories: [],
      selectedCategories: []
    }
  },
  mutations: {
    updateLocation (state, payload) {
      state.surprise.startLocation.id = payload.id;
      state.surprise.startLocation.name = payload.name;
    },
    updateDate (state, payload) {
      state.surprise.startDate = payload.startDate;
    },
    updateCategories (state, payload) {
      state.surprise.categories = payload.categories;
    },
    updateCategorySelection (state, payload) {
      state.surprise.selectedCategories = payload.categories;
    }
  },
  actions: {
    async getCategories (context) {
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
    async postSurprise (context) {
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
    }
  }
})
