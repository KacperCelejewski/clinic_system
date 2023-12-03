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
          <div class="form-group mt-3">
            <button type="submit" class="btn btn-primary btn-lg btn-block">
              {{ patient.loading ? "Submitting..." : "Submit" }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      patient: {
        loading: false,
        name: "",
        surrname: "",
        error: null,
        message: null,
        pesel: this.$route.params.pesel,
      },
    };
  },

  methods: {
    async getPatient() {
      const patientPesel = this.patient.pesel;
      this.patient.loading = true;

      try {
        const response = await axios.get(
          "http://localhost:5000/search-patient",
          {
            headers: {
              "Content-Type": "application/json",
              pesel: this.pesel,
            },
          }
        );

        this.patient.name = response.data.name;
        this.patient.surrname = response.data.surrname;
        this.patient.loading = false;
      } catch (error) {
        console.error("Error while fetching patient data:", error);
        this.patient.error = error.message || "An error occurred";
      }
    },

    async checkForm() {
      if (this.patient.name && this.patient.surrname) {
        this.patient.loading = true;

        try {
          await this.$http.put(`http://localhost:5000/search-patient/edit`, {
            name: this.patient.name,
            surrname: this.patient.surrname,
            pesel: this.patient.pesel,
          });

          this.patient.name = "";
          this.patient.surrname = "";
          this.patient.message = "Patient edited successfully";
        } catch (error) {
          console.error("Error while editing patient:", error);
          this.patient.error = error.message || "An error occurred";
        } finally {
          this.patient.loading = false;
        }
      } else {
        this.patient.error = !this.patient.name
          ? "Name is required"
          : "Surname is required";
      }
    },
  },

  mounted() {
    this.getPatient();
  },
};
</script>
