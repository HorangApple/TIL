function validateEmail(email){
    return email.match(/@/) ?
        email :
        new Error(`invalid email: ${email}`);
}

const email = "janedoe.com";

const validatedEmail = validateEmail(email);
if(validatedEmail instanceof Error){
    console.error(`Error: ${validatedEmail.message}`);
} else {
    console.log(`Valid email: ${validatedEmail}`);
}