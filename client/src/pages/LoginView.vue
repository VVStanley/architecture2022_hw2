<template>
  <div class="alert" :class="[ classAlert ? classAlert : '' ]" role="alert">
    {{ textAlert }}
  </div>
  <form class="form-control col-md-3" @submit.prevent="loginSubmit">
    <input type="text" v-on:focus="changeInputs" v-model="user.username"
           placeholder="username" class="form-control" name="username">
    <input type="text" v-on:focus="changeInputs" v-model="user.password"
           placeholder="password" class="form-control" name="password1">
    <button class="btn btn-success">Submit</button>
  </form>

  <hr>
  <button>кнопка</button>

</template>

<script>
import axios from "@/axios/index";
import store from "@/store";

export default {
  name: 'LoginView',
  data() {
    return {
      classAlert: '',
      textAlert: '',
      user: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    changeInputs() {
      this.classAlert = '';
      this.textAlert = ''
    },
    async loginSubmit() {
      console.log(this.user)
      if (
          this.user.username === '' ||
          this.user.password === ''
      ) {
        this.classAlert = 'alert-danger';
        this.textAlert = 'Заполните поля'
      } else {
        let username = this.user.username;
        let password = this.user.password;
        await axios.post(
            '/auth/sign-in/',
            `grant_type=&username=${username}&password=${password}`,
            {
              headers: {"Content-Type": "application/x-www-form-urlencoded"}
            }
        ).then(
            ({data}) => {
              store.commit('setAuthToken', data.access_token);
              window.location.reload();
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
