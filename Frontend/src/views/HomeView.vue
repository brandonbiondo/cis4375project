<template>
  <div class="grocery-store-home">
    <h1 style="font-size: 60px">Hisway African Grocery Store</h1>
    <div class='start'>
      <h3 style="font-size: 20px"> Grocery Store in Katy </h3>
      <h3 style="font-size: 20px"> Open today until 8:00 PM </h3>
      <div>
        <router-link to="/quote">
        <v-btn color= "#5f9bce" light>Get Quote</v-btn>
        </router-link>
      </div>
      <br>
    </div>
    <br>
    <div class='main'>
    <img src = 'https://lh3.googleusercontent.com/p/AF1QipNVh7_zlLdspQ1mXFGFsvZdv64oUX9qB0d-q47k=w1080-h608-p-no-v0'>
    </div>
    <br>
    <h1> Updates </h1>
    <div class="category-list">
      <div class="category" v-for="category in categories" :key="category.id">
        <img :src="category.image" alt="category.name">
        <div class="category-name">{{ category.name }}</div>
        <div class="description">{{category.description}}</div>
      </div> 
    </div>

    <!-- view all link -->
  <div>
    <v-container>
      <v-row justify="center">
        <v-col cols="auto">
          <a href="https://www.google.com/search?q=Hisway+African+Grocery+Store&ludocid=2196565002355305937&lpsid=8204640617876253184&source=sh/x/localposts&lsig=AB86z5UuY2ZQapFTf79I9WXM4AOd" style="font-size: 24px; color: #5f9bce;">VIEW ALL</a>
        </v-col>
      </v-row>
    </v-container>
  </div>

    <h1> Testimonials </h1>
    <div>
      <v-container>
        <v-row>
          <v-col cols="4" v-for="review in reviews" :key="review.id"> <!-- loop through reviews and create a column for each -->
            <div class="review">
              <img src="https://th.bing.com/th/id/R.36e80f72679a659cd22653336fb5cd56?rik=9eeQWNNmLk2TSw&riu=http%3a%2f%2fclipart-library.com%2fimages_k%2f5-stars-transparent-background%2f5-stars-transparent-background-1.png&ehk=q4WEQOMxc46KcpzEvo2Fw70LtaxoD%2fSU6T5JsFk24bQ%3d&risl=&pid=ImgRaw&r=0" alt="5 stars" class="stars-image">
              <p class="review-text">{{ review.text }}</p>
              <p class="review-text">{{review.name}}</p>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>

<!-- 2 links -->
  <div>
    <v-container>
      <v-row justify="center">
        <v-col cols="auto">
          <a href="https://www.google.com/search?hl=en-US&gl=us&q=Hisway+African+Grocery+Store,+3507+Paintbrush+Dawn+Ct,+Katy,+TX+77493&ludocid=2196565002355305937&lsig=AB86z5VTmhcTAe3N-Wg0DsFynK9t#lrd=0x864127667b37dced:0x1e7bc43b53716dd1,3" style="font-size: 24px; color: #5f9bce;">WRITE A REVIEW</a>
        </v-col>
        <v-col cols="auto">
          <a href="https://www.google.com/search?q=Hisway+African+Grocery+Store&ludocid=2196565002355305937&source=sh/x/localposts&lsig=AB86z5UuY2ZQapFTf79I9WXM4AOd#lrd=0x864127667b37dced:0x1e7bc43b53716dd1,1,,,," style="font-size: 24px; color: #5f9bce; ">READ MORE</a>
        </v-col>

      </v-row>
    </v-container>
  </div>

     <h1> Gallery </h1>
      <div class="food-list">
      <div class="food" v-for="food in foods" :key="food.id">
        <img :src="food.image" alt="food.name">
      </div>      

      </div>

    <h1> Contact Us </h1>
    <br>
      <div style="text-align: center;">
        <img src="https://scontent-dfw5-2.xx.fbcdn.net/v/t39.30808-6/229505446_10165334602810277_990418285611305810_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=e3f864&_nc_ohc=8KvYAs7YvukAX_2jh8x&_nc_ht=scontent-dfw5-2.xx&oh=00_AfCETTTREROhvlYgWCOCKR2IseXeEjqWccox91KE3RB88Q&oe=64357818" 
        alt="Hisway_logo" :style="{ width: imageSize + 'px', height: 'auto' , }">
      </div>
      <br>
      <div>
        <v-container> 
          <v-row justify="center"> 
            <v-col cols="auto">
              <h3 style="font-size: 20px"> Contact </h3>
                <v-btn variant="text" href="tel:+1-832-542-2551">
                    <div class="d-flex mr-1">
                        <v-icon icon="mdi-phone"></v-icon>
                    </div>
                    <span>Call Now</span>
                </v-btn>              
              <p> (832) 542 2551 </p>
            </v-col>
            <v-col cols="auto">
              <h3 style="font-size: 20px"> Address </h3>
                <v-btn @click="window.location.href='https://www.google.com/maps/dir//Hisway+African+Grocery+Store/data=!4m8!4m7!1m0!1m5!1m1!1s0x864127667b37dced:0x1e7bc43b53716dd1!2m2!1d-95.7781103!2d29.822653499999998'" variant="text">
                    <div class="d-flex mr-1">
                        <v-icon icon="mdi-directions"></v-icon>
                    </div>
                    <span>Get Directions</span>
                </v-btn>
                  <p>3507 Paintbrush Dawn Court</p>
                  <p>Katy, TX 77493</p>
                  <p>USA</p>                              
            </v-col>
            <v-col cols="auto"> 
              <h3 style="font-size: 20px"> Business Hours </h3>
              <p>Mon:	10:00 AM – 8:00 PM </p>
              <p>Tue:	10:00 AM – 8:00 PM </p>
              <p>Wed:	10:00 AM – 8:00 PM </p>
              <p>Thu:	10:00 AM – 8:00 PM </p>
              <p>Fri:	10:00 AM – 7:00 PM </p>
              <p>Sat:	9:00 AM – 8:00 PM </p>
              <p>Sun:	Closed </p>

            </v-col>
          </v-row>
        </v-container>
      </div>  
  </div>    
</template>

<script>
export default {
  data() {
    return {
        imageSize: 500,

      categories: [
        {
          id: 1,
          name: 'Posted on Mar 28, 2023',
          description: 'Beannygold flour is now available!',
          image: 'https://lh3.googleusercontent.com/p/AF1QipM9plJMCBqavSIAudLRiLwxDvgaRpK_BEzPgqHy=w600-h0'
        },
        {
          id: 2,
          name: 'Posted on Feb 28, 2023',
          description: 'Fresh ripe plantain',
          image: 'https://lh3.googleusercontent.com/p/AF1QipPHWqUZvcSEhGd1pgA_lBc554q2iQJj7nD9fUyp=w600-h0'
        },
        {
          id: 3,
          name: 'Posted on Dec 13, 2022',
          description: 'Indomie noodles is back in stock. Holidays is arond the corner, stock up now.',          
          image: 'https://lh3.googleusercontent.com/p/AF1QipNrUa99crA0YgOFt8vV7WpdleoVPz1e8pUfkxby=w600-h0'
        },
        {
          id: 4,
          name: 'Posted on Dec 13, 2022',
          description: 'Dear customer, Par Excellence rice is back in stock. It is available in 25lbs and 50lbs',          
          image: 'https://lh3.googleusercontent.com/p/AF1QipO8SJ0chtIXiMpryMO4UUROQTyss-44jLwAOWBw=w600-h0'
        },
        {
          id: 5,
          name: 'Posted on Aug 20, 2022',
          description: 'Hello wonderful people. We are open and we have your favorite African products.',          
          image: 'https://lh3.googleusercontent.com/p/AF1QipMjswS78Ral6axLVEDiLVKOchIum9BIVqMePuC7=w600-h0'
        },
        {
          id: 6,
          name: 'Posted on Aug 20, 2022',
          description: 'Hello folks. We are open and we have your favorite African products. We have fresh snail, new yam, fesh Jolly Jolly bread, Para Excellence Rice (different sizes), egg plant, and so many more.',          
          image: 'https://lh3.googleusercontent.com/p/AF1QipOYJxmb7es-n8enjYqcbA6REwAauaHlUsafkurO=w600-h0'
        }
      ],
      foods: [
        {
        id: 1,
        image: 'https://lh3.googleusercontent.com/p/AF1QipPKz1PFfWK-srKrEnTrTYSKBwLeiTtZ-_SnXvL6=w960-h960-n-o-v1'
        },
        {
        id: 2,
        image: 'https://lh3.googleusercontent.com/p/AF1QipOCxqi4mvlVybSpt1kn7osBK4n-IEvxB2CUF88E=w960-h960-n-o-v1'
        },
        {
        id: 3,
        image: 'https://lh3.googleusercontent.com/p/AF1QipNomBKG0GeMbTiJrA-tjKFPNLaiAQrPwQ5SpfCD=w960-h960-n-o-v1'
        },
        {
        id: 4,
        image: 'https://lh3.googleusercontent.com/p/AF1QipOlN1C5coX7LhxtGlx2rotbmFd0E5Kn4axCTST7=w960-h960-n-o-v1'
        },
        {
        id: 5,
        image: 'https://lh3.googleusercontent.com/p/AF1QipPCx2YAfr6WGRdiA-xyvhzMoZnKFw10oEFYOkRS=w960-h960-n-o-v1'
        },
        {
        id: 6,
        image: 'https://lh3.googleusercontent.com/p/AF1QipOzL77eBO7ru0AEYVyOlOiktMLfceecTPaUSvh8=w960-h960-n-o-v1'
        },
        {
        id: 7,
        image: 'https://lh3.googleusercontent.com/p/AF1QipNbqIZWnsQgYUQEx6e05Z3jyp6PE0p4zGCzutDj=w960-h960-n-o-v1'
        },
        {
        id: 8,
        image: 'https://lh3.googleusercontent.com/p/AF1QipOssy02-DQavUtlA-JTmd25GIn-dkgGH_AJ2pni=w960-h960-n-o-v1'
        },
        {
        id: 9,
        image: 'https://lh3.googleusercontent.com/p/AF1QipOviEoODp5ALa751KGQqENaK5dQjp0nLwjn8LUH=w960-h960-n-o-v1'
        },
      ],
      reviews: [ // sample review data
        { id: 1, 
          text: "The BEST African grocery store in H-Town hands down. They have great price you can never beat. Everything you get here is original, organic and fresh made. Once you try their products you will never go to another African store AGAIN! Oh did I mention wonderful customer service 💯.", 
          rating: 5, 
          name:"- Helen O." 
        },
        { id: 2, 
          text: "Best African store I've been to in Katy and Houston! The quality of their food stuff is second to none. Their palm oil, garri, elubo is the very best. I've been to almost every African Store in Houston but their products stand out in quality. I also like that I can call to place my order and just pick up when i arrive.", 
          rating: 5,
          name: "- Marcus O." 
          },
        { id: 3, 
          text: "Best African store in katy area pls order for any kind of African fresh food they will deliver to your doorstep. I really love all there stuff is very affordable . Africans raw foods.", 
          rating: 5,
          name: "- Tope P." },
      ]    
    }
  }
}
</script>

<style scoped>
@import url('https://cdn.jsdelivr.net/npm/@mdi/font@5.x/css/materialdesignicons.min.css');

.grocery-store-home {
  max-width: 1200px;
  margin: 0 auto;
  font-display: stencil;
}

h1 {
  font-size: 36px;
  margin-bottom: 30px;
  text-align: center;
  font-family: stencil;
  color: #5f9bce;
  margin-top: 70px;
}

.category-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.food-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.category {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  margin: 0 auto;
  max-width: 1000px;
  width: calc(33.33% - 97px);
  margin-bottom: 40px;
  text-align: center;
}

.food {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  margin: 0 auto;
  max-width: 1000px;
  width: calc(33.33% - 97px);
  margin-bottom: 40px;
  text-align: center;
}


.category img {
  width: 300px;
  height: 300px;
  object-fit: cover;
  margin-bottom: 10px;
  
}

.food img {
  width: 300px;
  height: 300px;
  object-fit: cover;
  margin-bottom: 10px;
  
}

.category-name {
  font-size: 20px;
  font-weight: bold;
  text-align: left;
  color: #5f9bce;
}

.main
{
  display: flex;
  justify-content: center;
}

.description
{
  font-size: 16px;
  text-align: justify;

}

.start
{
  text-align: center;
}


.stars-image {
  width: 100px;
  height: auto;
}

.review {
  margin-bottom: 20px;
}


</style>
