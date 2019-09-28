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
      startLocation: {
        id: null,
        name: null
      },
      categories: []
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
    }
  },
  actions: {

  }
})
