import {createStore} from 'vuex'

export default createStore({
  state: {
    authToken: localStorage.getItem('authToken') || null
  },
  getters: {
    isAuth: (state) => state.authToken
  },
  mutations: {
    setAuthToken(state, token) {
      localStorage.setItem('authToken', token);
      state.auth = true;
    },
  },
  actions: {},
  modules: {}
})
