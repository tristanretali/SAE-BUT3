export interface User {
	username: string;
	email: string;
	password: string;
	isSuperuser: boolean;
}

export type Role = "user" | "admin";
