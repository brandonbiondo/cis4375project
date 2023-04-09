<template>
  <div>
    <h1>Request a Quote</h1>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="name" required>
      </div>
      <div class="form-group">
        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" v-model="phone" required>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required>
      </div>
      <div class="form-group">
        <label for="message">How can we help you?</label>
        <textarea id="message" v-model="message" required></textarea>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      phone: '',
      email: '',
      message: ''
    };
  },
  methods: {
        submitForm() {
      const data = {
        name: this.name,
        phone: this.phone,
        email: this.email,
        message: this.message
      }
      axios.post('/api/quote', data)
        .then(response => {
          alert('Thank you for your inquiry. We will get back to you soon.');
          this.name = '';
          this.phone = '';
          this.email = '';
          this.message = '';
        })
        .catch(error => {
          console.log(error);
          alert('There was an error submitting the form. Please try again later.');
        });
    }
  }
}
</script>

<style>
@import url('https://cdn.jsdelivr.net/npm/@mdi/font@5.x/css/materialdesignicons.min.css');
.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
}

input,
textarea {
  display: block;
  width: 100%;
  padding: 0.5rem;
  border-radius: 0.25rem;
  border: 1px solid #ccc;
  font-size: 1rem;
  line-height: 1.5;
}

button[type="submit"] {
  background-color: #4751ff;
  color: #fff;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  border: none;
  font-size: 1rem;
  line-height: 1.5;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #3e8e41;
}

textarea {
  height: 10rem;
}
</style>
