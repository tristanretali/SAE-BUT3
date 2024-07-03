"use client"

import { User } from '@/lib/user';
import { getUser } from '@/lib/utils';
import { useQuery } from '@tanstack/react-query';
import { createContext, useContext, useEffect, useState } from 'react';

const AuthContext = createContext({
	auth: null,
	setAuth: (auth: any) => {},
	user: undefined as User | undefined | null,
});

export const useAuth = () => useContext(AuthContext);

interface AuthProviderProps {
	children: React.ReactNode;
}

const AuthProvider = ({ children }: AuthProviderProps) => {
	const [auth, setAuth] = useState(null);

	const { data: user } = useQuery<User>({
		queryKey: ["currentUser", auth],
		queryFn: async () => {
			return await getUser();
		},
	});
	
	return (
		<AuthContext.Provider value={{ auth, setAuth, user}}>
			{children}
		</AuthContext.Provider>
	);
};

export default AuthProvider;