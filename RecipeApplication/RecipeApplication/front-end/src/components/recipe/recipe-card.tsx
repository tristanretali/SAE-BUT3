import Image from "next/image";
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "../ui/card";
import { Button } from "@/components/ui/button";
import { Icons } from "@/components/icons";
import { RecipeFavorite } from "./recipe-favorite";
import { RecipeTag } from "./recipe-tag";
import { Recipe } from "@/lib/recipe";

type RecipeCardProps = {
	recipe: Recipe;
}

export function RecipeCard({recipe}: RecipeCardProps) {

	const getDiet = () => {
		const diet = recipe.vegan ? "vegan" : recipe.vegetarian ? "vegetarian" : null;
		if (!diet) return null;
		const DietIcon = Icons[diet];
		return {
			name: diet,
			icon: <DietIcon className="h-4 w-4"/>
		}
	}

	return (
		<Card className="relative">
			<RecipeFavorite/>
			<CardHeader className="p-0 mb-2">
				<Image src={recipe.image || "https://images.pexels.com/photos/9013258/pexels-photo-9013258.jpeg"} alt={recipe.title} className="rounded-t-md w-full select-none object-cover h-44" width={200} height={200}/>
			</CardHeader>
			<CardContent className="space-y-4 overflow-hidden">
				<CardTitle className="text-lg font-bold text-foreground truncate" title={recipe.title}>{recipe.title}</CardTitle>
				<div className="w-full text-muted-foreground flex *:flex-1 space-x-3">
					<RecipeTag value={recipe.servings}>
						<Icons.servings className="h-4 w-4"/>
					</RecipeTag>
					<RecipeTag value={recipe.readyInMinutes?.toFixed(0)} valueSuffix="min">
						<Icons.time className="h-5 w-5" width={50}/>
					</RecipeTag>
					<RecipeTag className="bg-green-200 text-lime-600 overflow-hidden whitespace-nowrap" value={getDiet()?.name}>
						{getDiet()?.icon}
					</RecipeTag>
				</div>
			</CardContent>
			<CardFooter>
				<Button className="w-full">
					<Icons.cooking className="mr-2 h-4 w-4" /> cook it!
				</Button>
			</CardFooter>
		</Card>
	)
}