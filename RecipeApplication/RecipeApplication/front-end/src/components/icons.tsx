import { BarChart, BarChart2, ChevronLeft, CookieIcon, CookingPot, CookingPotIcon, CreditCard, HeartIcon, LeafyGreenIcon, Lock, LogOut, LucideIcon, Shield, Star, StarIcon, TimerIcon, User, Users, VeganIcon } from "lucide-react";

export type Icon = LucideIcon;

export const Icons = {
	login: Lock,
	logout: LogOut,
	user: User,
	role: Shield,
	billing: CreditCard,
	chevronLeft: ChevronLeft,
	users: Users,
	analytics: BarChart,
	cooking: CookieIcon,
	rating: StarIcon,
	time: TimerIcon,
	vegan: VeganIcon,
	vegetarian: LeafyGreenIcon,
	like: HeartIcon,
} as const;