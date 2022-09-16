<template>
  <h1>Космический бой!</h1>
  <hr>
  <nav class="mb-5">
    <div v-if="$store.getters.isAuth">
      <router-link to="/fights">Fights</router-link>

    </div>
    <div v-else>
      <router-link to="/">Login</router-link>
      |
      <router-link to="/register">Register</router-link>
    </div>

  </nav>
  <router-view/>

</template>


<script>

</script>