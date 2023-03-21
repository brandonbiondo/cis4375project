<template>
    <div>
      <v-row>
      <v-col>
        <v-text-field v-model="search" label="Search" append-icon="mdi-magnify" />
      </v-col>
    </v-row>
    <h1 style="color: purple;">Vendors</h1>
    <v-table>
      <thead>
            <tr>
                <th>Vendor Name</th>
                <th>Phone</th>
                <th></th>
            </tr>
        </thead>
        <tbody>
          <tr v-for="vendor in vendors" :key="index">
              <td>{{ vendor.vendor_name }}</td>
              <td>{{ vendor.vendor_phone }}</td>
              <td>
                <v-icon small class="mr-2" @click="editVendor(item)">mdi-pencil</v-icon>
              <v-icon small class="mr-2" @click="deleteVendor(item)">mdi-delete</v-icon>
            </td>
          </tr>
          </tbody>
    </v-table>
    </div>
  </template>
  
  <script>

  export default {
    data() {
      return {
        headers: [
          { text: "Vendor Name", value: "vendor_name" },
          { text: "Vendor Phone", value: "vendor_phone" },
          { text: "Actions", value: "actions", sortable: false },
        ],
        vendors:[
        {
         vendor_name: "Bukky Enterprise", 
         vendor_phone:"281-552-2582"
        },
        {
         vendor_name: "Bomir Foods",
         vendor_phone:"931-683-7673"  
        },
        {
         vendor_name: "Spicy World", 
         vendor_phone:"832-752-8625"  
        },
        {
         vendor_name: "Fesojaye", 
         vendor_phone:"281-883-7728"  
        },
      ],
      
    };
  },
    methods: {
    editVendor(vendor) {
      const index = this.vendor.findIndex((vendor)=>vendor.vendor_name
      ===this.editingVendor.vendor_name && vendor.vendor_phone);
      if (index >= 0) {
        this.vendors.splice(index,1,this.editingVendor)
        this.$dialog.prompt({
          title: "Edit Vendor",
          body: "Enter new vendor information:",
          initialValue: `${vendor.vendorName},${vendor.vendorPhone}`,
          persistent: true,
        }).then((dialogData) => {
          const [vendorName, vendorPhone] = dialogData.split(",");
          this.vendor[index] = { ...this.vendor[index], vendorName, vendorPhone };
          this.$toast.success("Vendor updated successfully.");
        });
      }
    },
    deleteVendor(vendor) {
      const index = this.vendor.findIndex((v) => v.id === vendor.id);
      if (index >= 0) {
        this.$dialog
          .confirm({
            title: "Delete Vendor",
            message: `Are you sure you want to delete ${vendor.vendorName}?`,
            persistent: true,
          })
          .then(() => {
            this.vendor.splice(index, 1);
            this.$toast.success("Vendor deleted successfully.");
          });
      }
    },
  },
};
</script>












































