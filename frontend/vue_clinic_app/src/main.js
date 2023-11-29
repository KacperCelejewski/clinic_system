import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
import { createRouter, createWebHistory } from 'vue-router';
import PatientsList from './components/PatientsList.vue';
import AddPatient from './components/AddPatient.vue';
import EditPatient from './components/EditPatient.vue';
const app = createApp(App);

// Set up axios as a global variable
app.config.globalProperties.$http = axios;

// Create the router instance
const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: PatientsList,
      name: 'home',
    },
    {
        path: '/add-patient',
        component: AddPatient,
        name: 'add',
      },
      {
        path: '/search-patient/:pesel/edit',
        component: EditPatient,
        name: 'edit',
      },
  ],
});

// Use the router plugin
app.use(router);

// Mount the app to the #app element
app.mount('#app');
