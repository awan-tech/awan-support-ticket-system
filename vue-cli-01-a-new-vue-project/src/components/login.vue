<template>
    <section>
        <div id="header" class="header">
        <center>
            <h2 class="header-h2">Awan Ticket System</h2>        
        </center>
    </div>
    <div class="container" >
        <form>
            <div class="form-div">
              <label for="account" class="form-label">帳號 | Account</label>
              <input type="text" class="form-control" id="account" required>
            </div>
            <div class="form-div">
              <label for="password" class="form-label">密碼 | Password</label>
              <input type="password" class="form-control" id="password" required>
            </div>
            <div>
                <button type="submit" class="form-btn" onclick="連結">登入 | Login</button>
            </div>
            <div>
                <font color="red">帳號密碼錯誤</font>
            </div>
           
        </form>
    </div>
    </section>
    
</template>

<script>
export default {
    data() {

    },
    methods: {

    },
}
</script>

<style>
.header{
  position: absolute;
  width: 100%;
  top: 0%;
  background-color:#e5e5e5;
  text-align: center;
  font-size:20px;
  font-family:Sans-serif;
}
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
