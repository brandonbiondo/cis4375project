import { defineStore } from "pinia";
import { router } from '../router/index.js';

export const useLoginStore = defineStore({
    id: 'login',
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        user: JSON.parse(localStorage.getItem('user')),
        returnUrl: null
    }),
    actions: {
        async login(username, password) {
            try {
                //replace this with actual request to the backend
                const fakeUser = {username: "username", password: "1234"}
                if (username === fakeUser.username && password === fakeUser.password) {
                    localStorage.setItem('user', JSON.stringify(fakeUser));
                    // redirect to inventory page
                    router.push(this.returnUrl || '/inventory');
                    this.user = fakeUser;
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
            console.log(this.user)
            return (this.user != null);
        }
    }
});