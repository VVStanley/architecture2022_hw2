<template>
  <div :class="[ classAlert ? classAlert : '' ]" role="alert">
    {{ textAlert }}
  </div>
  <h4>Боец:</h4>
  <ul>
    <li v-for="(field, key) in currentUser"> {{ key }}: {{ field }}</li>
  </ul>
  <button v-if="currentUser.ready_to_fight" class="btn btn-warning"
          v-on:click="readyToFight(false)">Хватит мочилова!
  </button>
  <button v-else class="btn btn-success" v-on:click="readyToFight(true)">
    Готов к битве!
  </button>
  <hr>
  <div>
    <div class="row">
      <div class="col-md-6">
        <h4>Свободные бойцы:</h4>
        <ul>
          <li v-for="fighter in fighters" class="my-2">
            {{ fighter }} |
            <button v-on:click="addFighters(fighter)"
                    class="btn btn-success btn-sm">Добавить ->
            </button>
          </li>
        </ul>
      </div>
      <div class="col-md-6">
        <h4>Команда</h4>
        <ul>
          <li v-for="fighter in team">{{ fighter }}</li>
        </ul>
      </div>
    </div>
    <div class="row">
      <div class="col-md-6">
        <h4>Создать битву</h4>
        <button v-if="team.length > 1" v-on:click="addFight"
                class="btn btn-success">Создать бой
        </button>
      </div>
      <div class="col-md-6">
        <h4>Активные бои</h4>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "@/axios/index";
import store from "@/store";


export default {
  name: 'FightView',
  data() {
    return {
      ws: null,
      fighters: [],
      team: [],
      ships: [],
      fight_data: {
        token: null,
        data: null
      },
      classAlert: '',
      textAlert: '',
      currentUser: {
        username: null,
        id: null,
        fight: null,
        ready_to_fight: null
      },
      commands: [
        "RotateBurnFuelCommand",
        "MoveBurnFuelCommand",
        "ShootCheckBulletCommand"
      ]
    }
  },
  currentUser: null,
  async created() {
    await this.getCurrentUser();
    this.ws = new WebSocket(`ws://localhost:8000/ws/${this.currentUser.id}`);
    this.ws.onmessage = this.onMessage
  },
  watch: {

    fight_data(newValue, oldValue) {
      this.sendFakeStep()
      setInterval(this.sendFakeStep, 1000);
    }
  },
  methods: {
    async sendFakeStep() {
      console.log('send')
      // let ship = this.ships[Math.floor(Math.random() * this.ships.length)];
      let ship = this.ships[0];
      let command = this.commands[Math.floor(Math.random() * this.commands.length)];
      console.log('command send - ', ship)
      let fakeCommand = {
        token: this.fight_data.token,
        step: {
          id: ship.id,
          command: "MoveBurnFuelCommand"
        }
      }
      this.ws.send(JSON.stringify(fakeCommand))
    },
    async addFight() {
      let f = {ids: this.team.map(fighter => fighter.id).join(',')}
      console.log(f)
      await axios.get(
          `/fights/add/?ids=${this.team.map(fighter => fighter.id).join(',')}`,
          {
            headers: {
              Authorization: 'Bearer ' + store.getters.isAuth
            }
          }
      ).then(
          ({data}) => {
            this.fight_data = data

            this.ships = this.fight_data.data.filter(item => item.name === "ship")
            console.log('FIGHT CREATED -- ', this.ships);

          }
      ).catch(
          error => {
            this.classAlert = 'alert alert-danger';
            this.textAlert = error.response
          }
      )
    },
    addFighters(add_fighter) {
      add_fighter = JSON.parse(add_fighter)
      let exists = this.team.some(fighter => fighter.id === add_fighter.id)
      if (!exists) this.team.push(add_fighter)
    },
    onMessage(event) {
      let response = JSON.parse(event.data)
      if ('fighters' in response) {
        this.fighters = response['fighters']
      }

    },
    async readyToFight(ready_to_fight) {
      this.currentUser.ready_to_fight = ready_to_fight
      await axios.post(
          '/fights/ready/',
          {
            username: this.currentUser.username,
            id: this.currentUser.id,
            fight: this.currentUser.fight,
            ready_to_fight: this.currentUser.ready_to_fight
          },
          {
            headers: {
              Authorization: 'Bearer ' + store.getters.isAuth
            }
          }
      ).then(
          responses => this.getCurrentUser()
      ).catch(
          error => {
            this.classAlert = 'alert alert-danger';
            this.textAlert = error.response
          }
      )
    },
    async getCurrentUser() {
      await axios.get(
          '/auth/user/',
          {
            headers: {
              Authorization: 'Bearer ' + store.getters.isAuth
            }
          }
      ).then(
          ({data}) => this.currentUser = data
      ).catch(
          error => {
            this.classAlert = 'alert alert-danger';
            this.textAlert = error.response
          }
      )
    }
  },
}
</script>