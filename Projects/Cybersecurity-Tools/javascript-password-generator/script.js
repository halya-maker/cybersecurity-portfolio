function generatePassword() {

    const length = document.getElementById("length").value;

    const characters =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%";

    let password = "";

    for (let i = 0; i < length; i++) {

        let randomIndex =
        Math.floor(Math.random() * characters.length);

        password += characters[randomIndex];
    }

    document.getElementById("result").innerText = password;
}
