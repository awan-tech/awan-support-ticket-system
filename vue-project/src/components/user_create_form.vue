<template>
    <div id="create-form-container">
        <!-- <div class>&bull; Keep in Touch &bull;</div> -->
        <div action="#" method="post" id="contact_form">
            <input type="form-text" placeholder="title" name="telephone" id="telephone_input" required>

            <div class="message">
                <textarea name="message" placeholder="I'd like to ask a question" id="message_input" cols="30" rows="5" required></textarea>
            </div>

            <div class="submit">
                <input type="submit" value="Send Message" id="form_button" />
            </div>
        </div>
    </div>
</template>

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