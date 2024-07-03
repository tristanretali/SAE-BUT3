import { User } from "@/lib/user";
import { Avatar, AvatarFallback, AvatarImage } from "./ui/avatar";

interface UserAvatarProps {
	user: User;
}

export default function UserAvatar({ user }: UserAvatarProps) {

	const getFallbackAvatar = () => {
		if (user) {
			return user.username.substring(0, 2).toUpperCase();
		}
		return "";
	}

	return (
		<Avatar>
			<AvatarImage src={""} alt={user.username} />
			<AvatarFallback>{getFallbackAvatar()}</AvatarFallback>
		</Avatar>
	)
}