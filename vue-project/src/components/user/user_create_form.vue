<template>
    <div id="create-form-container">
        <div action="#" method="post" id="contact_form">
            <div class="text">
            <input v-model="ticket_title" type="form-text" placeholder="title" name="telephone" id="telephone_input" required>
            </div>
            <div class="service-select">
                <select v-model="type">
                    <option>請選擇您需要的服務</option>
                    <option>1.AWS_EC2</option>
                    <option>2.AWS_VPC</option>
                    <option>3.AWS_Route53</option>
                    <option>4.AWS_Cloudfront</option>
                    <option>5.AWS_S3</option>
                    <option>6.Azure_SQL Database</option>
                    <option>7.Azure_App Service</option>
                    <option>8.Azure_Azure Active Directory</option>
                    <option>9.Azure_Azure Maps</option>
                    <option>10.Azure_VM</option>
                </select>
            </div>

            <div  class="message">
                <textarea v-model="ticket_content" name="message" placeholder="I'd like to ask a question" id="message_input" cols="30" rows="5" required></textarea>
            </div>
            <div class="submit">
                <input @click="submmitAndCreate" type="submit" value="Send Message" id="form_button" />
            </div>
        </div>
    </div>
</template>

<script>
export default {
    inject : [
        'userlogindata'
    ],
    data() {
        return {
            ticket_title : '',
            ticket_content : '',
            type : ''
        }
    },
    methods: {
        submmitAndCreate() {
            if ( this.ticket_title === '' || this.ticket_content === '' || this.type === '') {
                alert('請填好表格')
                return false ;
            }
            fetch('https://kdmm5wrtrb.execute-api.us-west-2.amazonaws.com/dev/api/tickets/create',{
                method: 'POST',
                headers : {
                    'Content-Type': 'application/json'
                },
                body :  JSON.stringify({
                "customer_id": this.userlogindata['id'],
                    "service_id": this.type.split('.')[0] ,
                    "ticket_title": this.ticket_title,
                    "ticket_content": this.ticket_content,
                    "urgency": '1'
                })
            })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .then((data) => { 
                console.log( data['data']['message'] )
                alert(data['data']['message'])
            })
            

            this.ticket_title = '' ;
            this.ticket_content = '' ;

            this.$router.push('/userhome')
        },
        testCreate() {
            const temp = {
                "customer_id": this.userlogindata['id'],
                    "service_id": '3',
                    "ticket_title": this.ticket_title,
                    "ticket_content": this.ticket_content,
                    "urgency": 1
            }
            console.log( temp )
        }
    },
}
</script>

<style scoped>
    #create-form-container {
        border: solid 3px #474544;
        width: 768px;
        margin: 60px auto;
        position: relative;
        top: -30px;
        left: -20px;
        height: 90vh;
    }
    #contact_form {
        padding: 37.5px;
        margin: 50px 0;
        position: relative;
        height: 100vh;
        display: flex;
        flex-direction: column ;
    }
    #telephone_input{
        display: flex;
        flex-direction: column ;
    }
    input[type='form-text'], [type='email'],textarea {
        background: none;
        border: none;
        border-bottom: solid 2px #474544;
        color: #474544;
        font-size: 1.000em;
        font-weight: 400;
        letter-spacing: 1px;
        margin: 0em 0 1.875em 0;
        padding: 0 0 0.875em 0;
        width: 100%;

    }

    textarea {
        line-height: 150%;
        height: 35vh;
        resize: none;
        width: 100%;
    }
    .service-select select{
         background: #c5c4c4;
         color: #111010;
         /* margin: 15px; */
         width: 100%;
         height: 100%;
         padding: 8px;
         position: relative;
         appearance: none;
         border: solid 2px #474544;
    }
    .message{
        margin-top: 5%;
    }
    
    ::-webkit-input-placeholder {
        color: #474544;
    }
    #form_button {
        position: relative;
        background: none;
        border: solid 2px #474544;
        color: #474544;
        cursor: pointer;
        display: inline-block;
        font-family: 'Helvetica', Arial, sans-serif;
        font-size: 0.875em;
        font-weight: bold;
        outline: none;
        padding: 20px 35px;
        text-transform: uppercase;
    }
    #form_button {
        height: 10vh;
        padding: 15px 25px;
    }
    #form_button:hover {
        background: rgb(153, 164, 112);
        color: #F2F3EB;
    }
    #submit{
        height: 100%;
    }

</style>