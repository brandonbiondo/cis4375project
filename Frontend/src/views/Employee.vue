<template>
  <div>
    <v-text-field
      v-model="search"
      label="Search"
      prepend-inner-icon="mdi-magnify"
      class="mb3-"
      dense
    ></v-text-field>
    <v-btn color="success" @click="newDialog = true">Add New Employee</v-btn>
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
        <tr v-for="(employee, index) in filteredEmployees" :key="index">
          <td>{{ employee.employee_firstname }}</td>
          <td>{{ employee.employee_lastname }}</td>
          <td>{{ employee.employee_phone }}</td>
          <td>{{ employee.employee_role }}</td>
          <td>{{ employee.employee_address }}</td>
          <td>{{ employee.employee_startdate }}</td>
          <td>{{ employee.employee_enddate }}</td>
          <td>
            <v-icon v-if="!employee.employee_endDate" color="green">mdi-check</v-icon>
            <v-icon v-else color="red">mdi-close</v-icon>
          </td>
          <td>
            <v-btn color="primary" @click="editEmployeeDialog(index)">Edit</v-btn>
            <v-btn color="error" @click="deleteEmployee(index)">Delete</v-btn>
          </td>
        </tr>
      </tbody>
    </v-table>

    <!-- Dialog for adding a new employee -->
    <v-dialog v-model="newDialog" max-width="2000">
      <v-card>
        <v-card-title>Add New Employee</v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <!-- Form fields for new employee details (First Name, Last Name, etc.) -->
              <v-col>


              <v-text-field v-model="newEmployee.employee_firstname" label="First Name"></v-text-field>
              </v-col>
              <v-col>


              <v-text-field v-model="newEmployee.employee_lastname" label="Last Name"></v-text-field>
              </v-col>
              <v-col>
              <v-text-field v-model="newEmployee.employee_phone" label="Phone"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field v-model="newEmployee.employee_role" label="Role"></v-text-field>



              </v-col>
              <v-col>
                <v-text-field v-model="newEmployee.employee_address" label="Address"></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="newEmployee.employee_startdate" label="Start Date"></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="newEmployee.employee_enddate" label="End Date"></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-btn color="blue darken-1" text @click="newDialog = false">Close</v-btn>
          <v-btn color="blue darken-1" text @click="saveNewEmployee">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <!-- Dialog for editing an employee -->
    <v-dialog v-model="editDialog" max-width="2000">
      <v-card>
        <v-card-title>Edit Employee</v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <!-- Form fields for new employee details (First Name, Last Name, etc.) -->
              <v-col>


                <v-text-field v-model="this.employees[editId].employee_firstname" label="First Name"></v-text-field>
              </v-col>
              <v-col>


                <v-text-field v-model="this.employees[editId].employee_lastname" label="Last Name"></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="this.employees[editId].employee_phone" label="Phone"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field v-model="this.employees[editId].employee_role" label="Role"></v-text-field>



              </v-col>
              <v-col>
                <v-text-field v-model="this.employees[editId].employee_address" label="Address"></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="this.employees[editId].employee_startdate" label="Start Date"></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="this.employees[editId].employee_enddate" label="End Date"></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-btn color="blue darken-1" text @click="editDialog = false">Close</v-btn>
          <v-btn color="blue darken-1" text @click="editEmployee(this.employees[editId])">Save</v-btn>
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
      employees: [],
      search: "",


editDialog: false,
      newDialog: false,
editingEmployee: null,
newEmployee: {
employee_firstname: '',
employee_lastname: '',
employee_phone: '',
employee_role: '',
employee_address: '',
employee_startdate: '',
employee_enddate: '',
  editId: null,
},
};
},
methods: {
    editEmployeeDialog(index) {
      this.editDialog = true;
      this.editId = this.employees.findIndex(x => x.employee_firstname === this.filteredEmployees[index].employee_firstname)
    },
editEmployee(item) {
  this.employees.splice(this.editId, 1, item)
  console.log(item)
  axios.put("http://localhost:5000/employees", item, {params: {"employee_id" :item.employee_id}})
  this.editDialog = false;
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

axios.delete("http://localhost:5000/employees", {params: {"employee_id": this.filteredEmployees[index].employee_id}})
  this.employees.splice(index, 1);
},
saveNewEmployee() {
this.employees.push(this.newEmployee);
this.newDialog = false;
  axios.post("http://localhost:5000/employees", this.newEmployee)
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
  computed: {
    filteredEmployees() {
      return this.employees.filter(p => {
        return p.employee_firstname.toLowerCase().indexOf(this.search.toLowerCase()) != -1;
      })},
  },
async mounted() {
const employeeData = await axios.get('http://localhost:5000/employees');
this.employees = employeeData.data;
},
};
</script>
