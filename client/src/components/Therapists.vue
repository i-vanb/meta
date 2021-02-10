<template>
  <div>
    <div v-bind:key="item.id" v-for="item in list">
      <TherapistCard v-bind:card_data="item"/>
    </div>
  </div>
</template>

<script>
import TherapistCard from "@/components/TherapistCard";

export default {
  name: "Therapists",
  components: {
    TherapistCard
  },
  props: ['list']
}
</script>

<style scoped>

</style>