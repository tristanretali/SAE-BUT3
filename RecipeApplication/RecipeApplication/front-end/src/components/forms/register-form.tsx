"use client";

import { Form, FormField } from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { PasswordInput } from "@/components/ui/password-input";

import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";

import { FormInput } from "./form-input";
import { useState } from "react";

import { register } from "@/lib/utils";
import { navigate } from "@/app/actions";
import { useToast } from "../ui/use-toast";
import { useAuth } from "../providers/auth-provider";

const registerFormSchema = z.object({
	username: z.string().min(1, "Username is required"),
	email: z.string().email("Invalid email address"),
	password: z.string().min(1, "Password is required").regex(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!-%*?&])[A-Za-z\d@$!-%*?&]{8,}$/, "Password must contain at least 8 characters, one letter, one number and one special character"),
	confirmPassword: z.string().min(1, "Please confirm your password")
}).refine(data => data.password === data.confirmPassword, {
	message: "Passwords do not match",
	path: ["confirmPassword"]
});

export function RegisterForm() {

	const { setAuth } = useAuth();
	const [isLoading, setIsLoading] = useState(false);
	const { toast } = useToast();

	const form = useForm<z.infer<typeof registerFormSchema>>({
		resolver: zodResolver(registerFormSchema),
		defaultValues: {
			email: "",
			username: "",
			password: "",
			confirmPassword: ""
		},
	});

	async function onSubmit(values: z.infer<typeof registerFormSchema>) {
		setIsLoading(true); 
		const signInResponse = await register(values);

		setIsLoading(false);
		if (!signInResponse) {
			toast({
				title: "Register failed",
				variant: "destructive"
			})
			return;
		}	

		setAuth(true);
		navigate("/login");
	}

	return (
		<Form {...form}>
			<form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
				<FormField name="username" render={({ field }) => (
					<FormInput label="Username">
						<Input placeholder="johndoe" {...field}/>
					</FormInput>
				)}>
				</FormField>
				<FormField name="email" render={({ field }) => (
					<FormInput>
						<Input placeholder="example@example.com" {...field}/>
					</FormInput>
				)}>
				</FormField>
				<FormField name="password" render={({ field }) => (
					<FormInput>
						<PasswordInput {...field}/>
					</FormInput>
				)}>
				</FormField>
				<FormField name="confirmPassword" render={({ field }) => (
					<FormInput label="Confirm password">
						<PasswordInput {...field}/>
					</FormInput>
				)}>
				</FormField>
				<Button className="w-full" type="submit" disabled={isLoading}>Register</Button>
			</form>
		</Form>
	)
}