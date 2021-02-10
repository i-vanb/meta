<template>
  <div class="container">
    <div class="photo_wrapper">
      <div class="center" v-if="card_data.photo === 'Нет фото'"><p>Нет Фото</p></div>
      <img v-else class="image" v-bind:src="card_data.photo">
    </div>
    <div class="info">
      <div class="info_name">
        <p>{{card_data.name}}</p>
      </div>
      <div class="info_methods">
        <div v-bind:key="method" v-for="method in card_data.methods" class="info_methods_tag">
          {{method}}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TherapistCard",
  props: ['card_data']
}

</script>

<style scoped>
.container {
  width: 720px;
  margin: 20px auto;
  padding: 50px 30px;
  background-color: #F6F4F0;
  display: flex;
  flex-direction: row;
  border-radius: 10px;
}
.info {
  padding: 0 20px 10px 20px;
  flex: 1;
}
.info_name {
  background-color: #FE8A66;
  margin-bottom: 20px;
  padding: 20px;
  text-align: center;
  border-radius: 5px;
  font-size: 18px;
  font-weight: bold;
}

.info_methods {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
.info_methods_tag {
  background-color: #FE8A66;
  padding: 5px;
  /*flex-grow: 1;*/
  margin: 5px;
  text-align: center;
  border-radius: 5px;
  color: #F6F4F0;
}

.photo_wrapper {
  width: 200px;
  height: 300px;
  background-color: #fafafa;
  text-align: center;
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.center {
  height: 100%;
  padding: 20px;
  font-size: 12px;
}

</style>