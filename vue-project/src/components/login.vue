<template>
    <section>
        <div class="container" >
            <form >
                <div class="form-div">
                <label for="account" class="form-label">帳號 | Account</label>
                <input v-model="username" type="text" class="form-control" id="account" required>
                </div>
                <div class="form-div">
                <label for="password" class="form-label">密碼 | Password</label>
                <input v-model="password" type="password" class="form-control" id="password" required>
                </div>
                <div>
                    <button @click.prevent="getData" type="submit" class="form-btn" >登入 | Login</button>
                </div>
                <div v-if="isUser === 'False'">
                    帳號密碼錯誤
                </div>
                <div v-else-if="isUser === 'True'">
                    登入成功
                </div>
            
            </form>
        </div>
    </section>
    
</template>

<script>
export default {
    props: {
      user: {
        type: String,
      },
    },    
    data() {
      return {
        userid : '',
        checkuser : '',
        checkpassword : '',
        username : '',
        password : '',
        role : '',
        isUser : 'null'
      }
    },
    methods: {
      
      getData() {
        console.log('test');
         fetch('https://mbsgp811h1.execute-api.us-east-2.amazonaws.com/test/helloworld',{
            method: 'GET',
            headers : {
                'Content-Type': 'application/json'
            },
            // body :  JSON.stringify({
            //   name : 'Larry'
            // })
            })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .then((data) => { 
                this.checkuser = data['name'] ;
                this.checkpassword = data['password'] ;
                this.role = data['role'] ;
                this.loginstatus() ;
            })
      },
      loginstatus() {
        if ( this.username === this.checkuser && this.password === this.checkpassword  ) {
          
          console.log('user and password fit') ;
          this.isUser = 'True' ;
          // console.log( this.username )
          this.$emit( 'loginSuccess', this.isUser, this.checkuser, this.role ) ;
          this.$router.push('/home')
        }
        else {
          console.log('faild') ;
          this.isUser = 'False' ;
        }

        this.username = '' ;
        this.password = '' ;
        
      },
      
    },
    emits : [
        'loginSuccess'
    ]
}
</script>

<style>
.container{
    padding: 25px;
    position: absolute;
    width: 33%;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    background-color: #e5e5e5;  
}


.form-div{
  padding-bottom: 1rem;
  width: 100%;
  display: inline-flex;
  flex-direction: column;
}

.form-label{
  font-family:sans-serif;
  width: 100%;
  padding-bottom: 0.5rem;
}

.form-control{
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #212529;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ced4da;
  border-radius: 0.25rem
}


.form-btn {
  float: right;
  align-items: center;
  background-clip: padding-box;
  background-color: #fa6400;
  border: 1px solid transparent;
  color: #000000;
  font-size: 16px;
  font-weight: 600;
  padding: calc(.875rem - 1px) calc(1.5rem - 1px);
  text-decoration: none;
  transition: all 250ms;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: baseline;
  width: auto;
  border-radius: 0.5rem;
}

.form-btn:hover,
.form-btn:focus {
  background-color: #fb8332;
}
.form-btn:active {
  background-color: #c85000;
  box-shadow: rgba(0, 0, 0, .06) 0 2px 4px;
  transform: translateY(0);
}
</style>
