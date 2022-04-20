<template>
    <div id="create-form-container">
        <!-- <div class>&bull; Keep in Touch &bull;</div> -->
        <div action="#" method="post" id="contact_form">
            <input v-model="ticket_title" type="form-text" placeholder="title" name="telephone" id="telephone_input" required>

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

        }
    },
    methods: {
        submmitAndCreate() {
            fetch('https://ukbemjsll9.execute-api.us-east-2.amazonaws.com/test/api/tickets/create',{
                method: 'POST',
                headers : {
                    'Content-Type': 'application/json'
                },
                body :  JSON.stringify({
                "customer_id": this.userlogindata['id'],
                    "service_id": '3',
                    "ticket_title": this.ticket_title,
                    "ticket_content": this.ticket_content,
                    "urgency": 1
                })
            })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .then((data) => { 
                console.log( data )
            })
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

<style>
    #create-form-container {
        border: solid 3px #474544;
        width: 768px;
        margin: 60px auto;
        position: relative;
        top: -30px;
        left: -20px;
    }
    #contact_form {
        padding: 37.5px;
        margin: 50px 0;
    }
    input[type='form-text'], [type='email'], select, textarea {
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
        height: 150px;
        resize: none;
        width: 100%;
    }
    ::-webkit-input-placeholder {
        color: #474544;
    }
    #form_button {
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
        padding: 15px 25px;
    }
    #form_button:hover {
        background: rgb(153, 164, 112);
        color: #F2F3EB;
    }

</style>