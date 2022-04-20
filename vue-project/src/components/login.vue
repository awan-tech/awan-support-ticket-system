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
      
      getData() {
        console.log('test');
         fetch('https://ukbemjsll9.execute-api.us-east-2.amazonaws.com/test/api/login',{
            method: 'POST',
            headers : {
                'Content-Type': 'application/json'
            },
            body :  JSON.stringify({
               'account' : this.username,
               'password' : this.password
            })
            })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .then((data) => { 
                
                if ( data['data']['error'] == '無此帳號或密碼' ) {
                  console.log( '登入失敗') ;
                  this.isUser = 'False'
                }
                else {
                  console.log( '登入成功')
                  this.checkuser = data['data']['name']
                  this.role = data['data']['role']
                  this.userid = data['data']['id']


                  this.loginstatus() ;
                }
                  
                // console.log( this.userdata[0] ) ;
                // this.checkuser = temp['name'] ;
                // this.checkpassword = temp['password'] ;
                // this.role = temp['role'] ;
                
            })
      },
      loginstatus() {
        // console.log('ttttttttt')
        // console.log( this.userdata  ) ;

        if ( this.role === 'Engineer' || this.role === 'Engineer Supervisor' )
            this.$router.push('/home')
        else 
          this.$router.push('/userhome')

        this.$emit( 'loginSuccess', this.userid, this.checkuser, this.role ) ;


        // if ( (this.username === this.userdata[0]['name'] && this.password === this.userdata[0]['password'] ) ) {
        //   this.checkuser = this.userdata[0]['name'] ;
        //   this.role = this.userdata[0]['role']
        //   console.log('user and password fit') ;
        //   this.isUser = 'True' ;
        //   // console.log( this.username )
        //   this.$emit( 'loginSuccess', this.isUser, this.checkuser, this.role ) ;
          
        // }
        // else {
        //   console.log('faild') ;
        //   this.isUser = 'False' ;
        // }

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
  background-color: rgb(153, 164, 112);
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
  background-color: rgb(149, 173, 50);
}
.form-btn:active {
  background-color: rgb(126, 153, 16);
  box-shadow: rgba(0, 0, 0, .06) 0 2px 4px;
  transform: translateY(0);
}
</style>
