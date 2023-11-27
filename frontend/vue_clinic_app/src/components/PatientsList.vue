<template>
  <div>
    <form v-if="patients.length === 0" @submit.prevent="submitForm">
      <label for="searchPatient">PESEL</label><br />
      <input
        v-model="pesel"
        id="searchPatient"
        type="text"
        placeholder="Enter patient's PESEL..."
      />
      <input type="submit" />
    </form>

    <div v-else>
      <!-- Display patient data here -->
      <div v-for="patient in patients" :key="patient.id">
        <!-- Display patient information as needed -->
        {{ patient.name }} - {{ patient.surrname }}
        <button @click="editPatient(patient.id)">Edit</button>
        <button @click="deletePatient(patient.id)">Delete</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pesel: "",
      patients: [],
    };
  },
  methods: {
    // ... your existing methods ...

    async submitForm() {
      try {
        const response = await this.$http.get(
          `http://localhost:8082/search-patient/${this.pesel}`
        );
        this.patients = response.data;
      } catch (error) {
        console.error(error);
      }
    },

    // ... your other methods ...
  },
  created() {
    // Call getData here if needed
    // this.getData();
  },
};
</script>

<style scoped>
/* Your existing styles */
</style>
