<template>
  <div id="app">
    <Therapists v-bind:list="list"/>
    <div v-if="list === null" class="content-center">
      Нет специалистов
    </div>
  </div>
</template>

<script>
import Therapists from "@/components/Therapists";
const axios = require('axios');

export default {
  name: 'App',
  components: {
    Therapists
  },
  data() {
    return {
      list: null
      //  [
      //   {
      //     id: 1,
      //     name: 'Первый',
      //     methods: ['secret method'],
      //     photo: [{'url': 'https://dl.airtable.com/.attachmentThumbnails/858d861294660b22f72d24e36de00dc5/189227b8'}]
      //   },
      //   {
      //     id: 2,
      //     name: 'Восточный',
      //     methods: ['secret method', 'another', 'therapy', 'music therapy', 'super', 'aqua-therapy'],
      //     photo: ['Нет фото']
      //   },
      //   {
      //     id: 3,
      //     name: 'Шаолинь',
      //     methods: ['secret method'],
      //     photo: ['Нет фото']
      //   },
      // ]
    }
  },
   mounted() {
    axios
      .get('http://127.0.0.1:5000/therapists')
      .then(response => (this.list = response.data.list)).then(()=>console.log(this.list))
  //   .then(response => console.log(response.data.list))
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.4;
}
.content-center {
  width: 400px;
  margin: 100px auto;
  font-size: 24px;
  font-weight: bold;
  color: #fafafa;
  background-color: #FE8A66;
  border-radius: 10px;
  padding: 50px;
  text-align: center;
}

</style>
