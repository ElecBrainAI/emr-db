// Vue 컴포넌트에서 API 요청하기 (예: PatientList.vue)
<template>
  <div>
    <ul>
      <li v-for="patient in patients" :key="patient.patient_id">
        <h3>{{ patient.patient_name }}</h3>
        <!-- 여기에 다른 환자 정보 표시 -->
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      patients: [],
    };
  },
  mounted() {
    axios.get('http://localhost:8000/api/patients/') // Django의 Patient API 엔드포인트
      .then(response => {
        this.patients = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  },
};
</script>
