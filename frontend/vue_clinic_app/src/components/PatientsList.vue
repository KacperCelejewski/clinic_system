<template>
  <div>
    <form @submit.prevent="submitForm">
      <label for="searchPatient">PESEL</label><br />
      <input
        v-model="pesel"
        id="searchPatient"
        type="text"
        placeholder="Enter patient's PESEL..."
      />
      <button type="submit" class="btn btn-primary">Search</button>
    </form>

    <div v-if="patients.length > 0">
      <div v-for="patient in patients" :key="patient.id">
        <p>Name: {{ patient.name }}</p>
        <p>Surname: {{ patient.surrname }}</p>
        <router-link
          class="btn btn-info"
          :to="{ name: 'edit', params: { pesel: patient.pesel } }"
        >
          Edit
        </router-link>

        <button @click="deletePatient(patient.id)" class="btn btn-danger">
          Delete
        </button>
      </div>
    </div>

    <div v-if="errorMessage" class="alert alert-danger mt-3">
      {{ errorMessage }}
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pesel: "",
      patients: [],
      errorMessage: null,
    };
  },
  methods: {
    async submitForm() {
      try {
        // Clear the patients array before making a new search
        this.patients = [];
        this.errorMessage = null;

        if (!this.pesel) {
          this.errorMessage = "Please enter a valid PESEL.";
          return;
        }

        // Make the request with the pesel
        const response = await this.$http.get(
          `http://localhost:5000/search-patient/${this.pesel}`
        );

        // Check if the response contains patient data
        if (response.data && response.data.patient) {
          this.patients.push(response.data.patient);
        } else {
          this.errorMessage = "Patient not found.";
        }
      } catch (error) {
        console.error("Error fetching patient data:", error);

        // Handle different error scenarios
        if (error.response && error.response.status === 404) {
          this.errorMessage = "Patient not found.";
        } else {
          this.errorMessage = "An error occurred, please try again later.";
        }
      }
    },

    async deletePatient(patientId) {
      try {
        // Make the request to delete the patient
        await this.$http.delete(
          `http://localhost:5000/search-patient/${patientId}/delete`
        );

        // Update the patients array after deletion
        this.patients = this.patients.filter(
          (patient) => patient.id !== patientId
        );
      } catch (error) {
        console.error("Error deleting patient:", error);
        this.errorMessage = "An error occurred while deleting the patient.";
      }
    },
  },
};
</script>
