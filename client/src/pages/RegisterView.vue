<template>
  <div class="alert" :class="[ classAlert ? classAlert : '' ]" role="alert">
    {{ textAlert }}
  </div>
  <form class="form-control col-md-3" @submit.prevent="registerSubmit">
    <input type="text" v-on:focus="changeInputs" v-model="user.username"
           placeholder="username" class="form-control" name="username">
    <input type="text" v-on:focus="changeInputs" v-model="user.password1"
           placeholder="password" class="form-control" name="password1">
    <input type="text" v-on:focus="changeInputs" v-model="user.password2"
           placeholder="password" class="form-control" name="password2">
    <button class="btn btn-success">Submit</button>
  </form>
</template>

<script>
import axios from "@/axios/index";
import store from "@/store";

export default {
  name: 'RegisterView',
  data() {
    return {
      classAlert: '',
      textAlert: '',
      user: {
        username: '',
        password1: '',
        password2: ''
      }
    }
  },
  methods: {
    changeInputs() {
      this.classAlert = '';
      this.textAlert = ''
    },
    async registerSubmit() {
      if (
          this.user.username === '' ||
          this.user.password1 === '' ||
          this.user.password2 === ''
      ) {
        this.classAlert = 'alert-danger';
        this.textAlert = 'Заполните поля'
      } else if (this.user.password1 !== this.user.password2) {
        this.classAlert = 'alert-danger';
        this.textAlert = 'Пароли не совпадают'
      } else {
        let data = {
          'username': this.user.username,
          'password': this.user.password1
        }
        await axios.post(
            '/auth/sign-up/', data
        ).then(
            ({data}) => {
              store.commit('setAuthToken', data.access_token)
            }
        ).catch(
            error => {
              this.classAlert = 'alert-danger';
              this.textAlert = error.response.data
            }
        )
      }
    }
  }
}
</script>
