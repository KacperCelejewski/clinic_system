<template>
  <div class="patient">
    <div class="container">
      <div class="row">
        <div class="col-sm-6 offset-sm-3">
          <!-- Showing the added todos -->

          <div v-if="patients.length == 0">
            <div class="patient mt-2 mb-2">
              <div class="patient-body">
                <h4 class="patient-name">Patients's list is empty</h4>
                <div class="d-flex justify-content-between">
                  <a class="btn btn-info text-white" href="/add-patient"
                    >Add patient</a
                  >
                </div>
              </div>
            </div>
          </div>

          <div
            v-else-if="patients.length > 0"
            v-for="patient in patients"
            v-bind:key="patient.id"
          >
            <div class="patient mt-2 mb-2">
              <div class="card-body">
                <h4 class="patient-name">{{ patient.name }}</h4>
                <p class="patient-surrname">{{ patient.surrname }}</p>
                <div class="d-flex justify-content-between">
                  <button
                    class="btn btn-info text-white"
                    @click="editPatient(patient.id)"
                  >
                    Edit
                  </button>
                  <button
                    class="btn btn-danger"
                    @click="deletePatient(patient.id)"
                  >
                    Delete
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      patients: [],
    };
  },
  methods: {
    async getData() {
      try {
        const response = await this.$http.get("http://localhost:8080/patient");
        this.patients = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async editPatient(patientId) {
      this.$router.push({
        path: `/edit-patient/${patientId}`,
      });
    },
    async deletePatient(patientId) {
      let confirmation = confirm("Do you want to delete this patient?");
      if (confirmation) {
        try {
          await this.$http.delete(
            `http://localhost:5000/api/patient/${patientId}`
          );
          this.getData();
        } catch (error) {
          console.error(error);
        }
      }
    },
  },
  created() {
    this.getData();
  },
};
</script>
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

.patient-body {
  text-align: left;
}

.patient {
  margin-top: 10px;
}
</style>
