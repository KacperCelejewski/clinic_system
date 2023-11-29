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
    getPatient: async function () {
      // the current patient id
      let patientPesel = this.patient.pesel;
      // start loading]
      console.log(patientPesel);
      this.patient.loading = true;
      // get the patient
      try {
        let response = await this.$http.get(
          `http://localhost:5000/search-patient/${patientPesel}`
        );
        this.patient.name = response.data.name;
        this.patient.surrname = response.data.surrname;
        this.patient.loading = false;
        return;
      } catch (error) {
        this.patient.error = error.message || "An error occurred";
        return;
      }
    },
    checkForm: async function (e) {
      // Custom validation\
      console.log(this.patient.pesel, "dd8d7u");
      if (this.patient.name && this.patient.surrname) {
        try {
          // send data to the server
          await this.$http.put(
            `http://localhost:5000/search-patient/${this.patient.pesel}/edit`,
            {
              name: this.patient.name,
              surrname: this.patient.surrname,
              pesel: this.patient.pesel,
            }
          );

          // reset the fields
          this.patient.name = "";
          this.patient.surrname = "";

          // set the message
          this.patient.message = "Patient edited successfully";

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
      e.preventDefault();
    },
  },
  mounted() {
    // Called after the component has been fully mounted
    this.getPatient();
  },
};
</script>
