import { User } from "@/lib/user";
import { Avatar, AvatarFallback, AvatarImage } from "./ui/avatar";

interface UserAvatarProps {
	user: User;
}

export default function UserAvatar({ user }: UserAvatarProps) {

	const getFallbackAvatar = () => {
		if (user) {
			return user.firstName.charAt(0) + user.lastName.charAt(0);
		}
		return "";
	}

	return (
		<Avatar>
			<AvatarImage src={""} alt={user.firstName} />
			<AvatarFallback>{getFallbackAvatar()}</AvatarFallback>
		</Avatar>
	)
}