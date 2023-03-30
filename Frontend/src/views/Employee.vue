<template>
  <div>
    <v-text-field
      v-model="search"
      label="Search"
      prepend-inner-icon="mdi-magnify"
      class="mb3-"
      dense
    ></v-text-field>
    <v-btn color="success" @click="dialog = true">Add New Employee</v-btn>
    <h1 style="color: blue;">Employees Page</h1>
    <v-table>
      <thead>
        <tr>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Phone</th>
          <th>Role</th>
          <th>Address</th>
          <th>Start Date</th>
          <th>End Date</th>
          <th>Status</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(employee, index) in employees" :key="index">
          <td>{{ employee.employee_firstName }}</td>
          <td>{{ employee.employee_lastName }}</td>
          <td>{{ employee.employee_phone }}</td>
          <td>{{ employee.employee_role }}</td>
          <td>{{ employee.employee_address }}</td>
          <td>{{ employee.employee_startDate }}</td>
          <td>{{ employee.employee_endDate }}</td>
          <td>
            <v-icon v-if="!employee.employee_endDate" color="green">mdi-check</v-icon>
            <v-icon v-else color="red">mdi-close</v-icon>
          </td>
          <td>
            <v-btn color="primary" @click="editEmployee(employee)">Edit</v-btn>
            <v-btn color="error" @click="deleteEmployee(index)">Delete</v-btn>
          </td>
        </tr>
      </tbody>
    </v-table>

    <!-- Dialog for adding a new employee -->
    <v-dialog v-model="dialog" max-width="600px">
      <v-card>
        <v-card-title>Add New Employee</v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <!-- Form fields for new employee details (First Name, Last Name, etc.) -->
              <v-text-field v-model="newEmployee.employee_firstName" label="First Name"></v-text-field>
              <v-text-field v-model="newEmployee.employee_lastName" label="Last Name"></v-text-field>
              <v-text-field v-model="newEmployee.employee_phone" label="Phone"></v-text-field>
              <v-text-field v-model="newEmployee.employee_role" label="Role"></v-text-field>
              <v-text-field v-model="newEmployee.employee_address" label="Address"></v-text-field>
              <v-text-field v-model="newEmployee.employee_startDate" label="Start Date"></v-text-field>
              <v-text-field v-model="newEmployee.employee_endDate" label="End Date"></v-text-field>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
          <v-btn color="blue darken-1" text @click="saveNewEmployee">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      headers: [
        { text: 'First Name', value: 'employee_firstName' },
{ text: 'Last Name', value: 'employee_lastName' },
{ text: 'Phone', value: 'employee_phone' },
{ text: 'Role', value: 'employee_role' },
{ text: 'Address', value: 'employee_address' },
{ text: 'Start Date', value: 'employee_startDate' },
{ text: 'End Date', value: 'employee_endDate' },
{ text: '', value: 'actions', sortable: false },
],
employees: [
{
employee_firstName: 'Elizabeth',
employee_lastName: 'Oyewale',
employee_phone: '832 629-0177',
employee_role: 'Owner/Manager',
employee_address: 'Redclove avenue 2000',
employee_startDate: '2022-06-01',
employee_endDate: '',
},
{
      employee_firstName: 'Steven',
      employee_lastName: 'Oyewale',
      employee_phone: '832 567-9029',
      employee_role: 'Assistant Manager',
      employee_address: 'Redclove avenue 2000',
      employee_startDate: '2022-06-01',
      employee_endDate: '',
    },
    {
      employee_firstName: 'Alice',
      employee_lastName: 'Oyebefun',
      employee_phone: '832 835-7227',
      employee_role: 'Cashier',
      employee_address: 'Redclove Avenue 2000',
      employee_startDate: '2022-06-01',
      employee_endDate: '',
    },
    {
      employee_firstName: 'Cruz',
      employee_lastName: 'Martinez',
      employee_phone: '832 257-7439',
      employee_role: 'Stocker',
      employee_address: 'Willow Dr 1527',
      employee_startDate: '2022-06-10',
      employee_endDate: '',
    },
    {
      employee_firstName: 'Maria',
      employee_lastName: 'Garza',
      employee_phone: '832 282-2758',
      employee_role: 'Cleaner',
      employee_address: 'Overbrook Ln 1950',
      employee_startDate: '2022-06-10',
      employee_endDate: '',
    },
  ],

dialog: false,
editingEmployee: null,
newEmployee: {
employee_firstName: '',
employee_lastName: '',
employee_phone: '',
employee_role: '',
employee_address: '',
employee_startDate: '',
employee_endDate: '',
},
};
},
methods: {
editEmployee(employee) {
this.editingEmployee = { ...employee };
this.dialog = true;
},
saveEmployee() {
const index = this.employees.findIndex(
(employee) =>
employee.employee_firstName === this.editingEmployee.employee_firstName &&
employee.employee_lastName === this.editingEmployee.employee_lastName
);
if (index >= 0) {
this.employees.splice(index, 1, this.editingEmployee);
}
this.dialog = false;
this.editingEmployee = null;
},
deleteEmployee(index) {
this.employees.splice(index, 1);
},
saveNewEmployee() {
this.employees.push(this.newEmployee);
this.dialog = false;
this.newEmployee = {
employee_firstName: '',
employee_lastName: '',
employee_phone: '',
employee_role: '',
employee_address: '',
employee_startDate: '',
employee_endDate: '',
};
},
},
async mounted() {
const employeeData = await axios.get('http://localhost:5000/employees');
console.log(employeeData.data);
this.employees = employeeData.data;
},
};
</script>
