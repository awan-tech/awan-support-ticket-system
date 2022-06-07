<template>
 
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
              <p style="color:red">帳號密碼錯誤  </p>
          </div>
          <div v-else-if="isUser === 'True'">
              登入成功
          </div>
      
      </form>
  </div>
   
    
</template>

<script>
import { Auth } from "aws-amplify";
export default {

  
    props: {
      user: {
        type: String,
      },
    },    
    data() {
      return {
        userdata : [],
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
      login() {
        try {
                const userObj = Auth.currentAuthenticatedUser() ;
                console.log( userObj ) ;
            }
            catch(err) {
                console.log( err )
            }
      },
      async getData() { 
        try{
          await Auth.signIn(
            this.username,
            this.password
          )

          console.log( '登入成功')
          const user = await Auth.currentUserInfo(); 
          if ( user != null ) {
              this.checkuser = user['attributes']['custom:name']
              this.role = user['attributes']['custom:role']
              this.userid = user['attributes']['custom:id']
              this.loginstatus() ;
          }
          else {
            console.log( '登入失敗') ;
            this.isUser = 'False'
          }

        }
        catch( err ) {
          console.log( err )
          console.log( '登入失敗') ;
          this.isUser = 'False'
        }

        //  await fetch('https://kdmm5wrtrb.execute-api.us-west-2.amazonaws.com/dev/api/login',{
        //     method: 'POST',
        //     headers : {
        //         'Content-Type': 'application/json'
        //     },
        //     body :  JSON.stringify({
        //        'account' : this.username,
        //        'password' : this.password
        //     })
        //     })
        //     .then( (response) => {
        //         if ( response.ok ) {
        //             return response.json() ;
        //         }
        //     })
        //     .then((data) => { 
                
        //         if ( data['data']['error'] == '無此帳號或密碼' ) {
        //           console.log( '登入失敗') ;
        //           this.isUser = 'False'
        //         }
        //         else {
        //           console.log( '登入成功')
        //           this.checkuser = data['data']['name']
        //           this.role = data['data']['role']
        //           this.userid = data['data']['id']

        //           
        //         }  
        //     })
        
      },
      loginstatus() {
   

        if ( this.role === 'Engineer' || this.role === 'Engineer Supervisor' )
            this.$router.push('/home')
        else 
          this.$router.push('/userhome')

        this.$emit( 'loginSuccess', this.userid, this.checkuser, this.role ) ;


        this.username = '' ;
        this.password = '' ;
        
      },
      
    },
    emits : [
        'loginSuccess'
    ]
}
</script>

<style scoped>
.container{
    padding: 3%;
    position: absolute;
    width: 33%;
    left: 50%;
    top: 40%;
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
