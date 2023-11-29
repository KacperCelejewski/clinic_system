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
        <p>Name:{{ patient.name }}</p>
        <p>Surrname: {{ patient.surrname }}</p>
        <router-link
          class="nav-link"
          :to="{ name: 'edit', params: { pesel: patient.pesel } }"
        >
          Edit
        </router-link>

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
    async submitForm() {
      try {
        if (this.pesel !== undefined) {
          const response = await this.$http.get(
            `http://localhost:5000/search-patient/${this.pesel}`
          );
          this.patients = response.data;
        } else {
          console.error("Pesel is undefined");
          // Handle the case where pesel is not defined
        }
      } catch (error) {
        console.error("Error fetching patient data:", error);
        // Display an error message to the user if needed
      }
    },
    // async editPatient() {
    //   try {
    //     const response = await this.$http.put(
    //       `http://localhost:5000/search-patient/${this.pesel}`
    //     );
    //     this.patients = response.data;
    //   } catch (error) {
    //     console.error(error);
    //   }
    // },

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
