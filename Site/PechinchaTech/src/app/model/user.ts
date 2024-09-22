export class User {
    id?: number;
    username: string;
    email: string;
    senha: string;

    constructor() {
        this.username = "";
        this.email = "";
        this.senha = "";
    }
}
