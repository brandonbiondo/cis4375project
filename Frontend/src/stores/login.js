import { defineStore } from "pinia";
import { router } from '../router/index.js';
import axios from "axios";

export const useLoginStore = defineStore({
    id: 'login',
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        user: JSON.parse(localStorage.getItem('user')),
        returnUrl: null,
        logins: [],
    }),
    getters: {
        getLogins(state){
            return state.logins
        }
    },
    actions: {
        async login(username, password) {
            await this.fetchLogins()
            try {
                //replace this with actual request to the backend
                const response = await axios.post("http://localhost:5000/check_login",  {"login_username": username, "login_password": password})
                const canLogin = response.data
                if (canLogin.authorized) {
                    localStorage.setItem('user', JSON.stringify( {"username": username, "password": password}));
                    // redirect to inventory page
                    router.push(this.returnUrl || '/inventory');
                    this.user = {"username": username, "password": password};
                    return true
                } else {
                    console.log("invalid credentials")
                }

            } catch (error) {
                console.log("error logging in")
                return false
            }
        },
        logout() {
            this.user = null;
            localStorage.removeItem('user');
            router.push('/');
        },
        isLoggedIn() {
            return (this.user != null);
        },
        async fetchLogins() {
            const response = await axios.get("http://localhost:5000/login")
            this.logins = response.data
        },
        async userHasLogin(employee_id) {
            return this.logins.some(i => i.employee_id == employee_id);
        }
    }
});