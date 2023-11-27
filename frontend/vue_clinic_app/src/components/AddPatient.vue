<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-6 offset-sm-3">
        <form
          id="patient-form"
          method="post"
          @submit.prevent="checkForm"
          novalidate="true"
        >
          <div v-if="patient.error" class="form-group mt-1">
            <div class="alert alert-danger">{{ patient.error }}</div>
          </div>
          <div v-if="patient.message" class="form-group mt-1">
            <div class="alert alert-success">{{ patient.message }}</div>
          </div>
          <div class="form-group mt-3" style="text-align: left">
            <label for="name">Name</label>
            <input
              v-model="patient.name"
              type="text"
              class="form-control"
              id="name"
              placeholder="Enter patient's name"
            />
            <small id="nameHelp" class="form-text text-muted">E.g., John</small>
          </div>
          <div class="form-group mt-3" style="text-align: left">
            <label for="surrname">Surname</label>
            <textarea
              v-model="patient.surrname"
              class="form-control"
              name="surrname"
              id="surrname"
              placeholder="Patient's surname"
            ></textarea>
            <small id="surrnameHelp" class="form-text text-muted"
              >E.g., Doe</small
            >
          </div>
          <div class="form-group mt-3" style="text-align: left">
            <label for="pesel">PESEL</label>
            <input
              v-model="patient.pesel"
              type="text"
              class="form-control"
              id="pesel"
              placeholder="Enter patient's PESEL"
            />
          </div>
          <div class="form-group mt-3">
            <button type="submit" class="btn btn-primary btn-lg btn-block">
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      patient: {
        name: "",
        surrname: "",
        error: null,
        message: null,
      },
    };
  },
  methods: {
    async checkForm() {
      if (this.patient.name && this.patient.surrname && this.patient.pesel) {
        try {
          // send data to the server
          await this.$http.post("http://localhost:8082/add-patient", {
            name: this.patient.name,
            surrname: this.patient.surrname,
            pesel: this.patient.pesel,
          });

          // reset the fields
          this.patient.name = "";
          this.patient.surrname = "";
          this.patient.pesel = "";

          // set the message
          this.patient.message = "Patient added successfully";

          return;
        } catch (error) {
          this.patient.error = error.message || "An error occurred";
          return;
        }
      }

      this.patient.error = null;
      if (!this.patient.name) {
        this.patient.error = "Name is required";
        return;
      }
      if (!this.patient.surrname) {
        this.patient.error = "Surname is required";
        return;
      }
      if (!this.patient.pesel) {
        this.patient.error = "PESEL is required";
        return;
      }
    },
  },
};
</script>
