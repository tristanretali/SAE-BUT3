import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";
import { API_URL } from "./constants";
import { User } from "./user";

const API_URL_AUTH = `${API_URL}/users`;

export function cn(...inputs: ClassValue[]) {
	return twMerge(clsx(inputs));
}

export const login = async (credentials: Pick<User, "username" | "password">) => {
	const response = await fetch(`${API_URL_AUTH}/login`, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		credentials: "include",
		body: JSON.stringify(credentials),
	});
	if (!response.ok) {
		return null;
	}
	return response.json();
};

export const register = async (credentials: Pick<User, "username" | "password"> & { confirmPassword: string }) => {
	const response = await fetch(`${API_URL_AUTH}`, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		credentials: "include",
		body: JSON.stringify(credentials),
	});
	if (!response.ok) {
		return null;
	}
	return response.json();
};

export const logout = async () => {
	const response = await fetch(`${API_URL_AUTH}/logout`, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		credentials: "include",
	});
	if (!response.ok) {
		return null;
	}
	return response.json();
};

export const getUser = async () => {
	const response = await fetch(`${API_URL_AUTH}/me`, {
		credentials: "include",
	});
	if (!response.ok) {
		return null;
	}
	return response.json();
};

String.prototype.toTitleCase = function () {
	return this.replace(/\w\S*/g, function (txt) {
		return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
	});
};

declare global {
	interface String {
		toTitleCase(): string;
	}
}
