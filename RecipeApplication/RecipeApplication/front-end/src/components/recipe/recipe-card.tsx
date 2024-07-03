import Image from "next/image";
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "../ui/card";
import { Button } from "@/components/ui/button";
import { Icons } from "@/components/icons";
import { RecipeFavorite } from "./recipe-favorite";
import { RecipeTag } from "./recipe-tag";

export type Recipe = {
	name: string
	recipeImage: string;
	rating: number;
	minutes: number;
	diet: string;
}

type RecipeCardProps = {
	recipe: Recipe;
}

export function RecipeCard({recipe}: RecipeCardProps) {

	const imageLink = "https://lh4.googleusercontent.com/proxy/2KLXzCX_ewTRnrg_6KEekqADDJ1Psjur6FfYDbDtwkEiXI0JUHkY4_-uHqIG88kAPnbohzqGO81m5ozytFS9mK3FkBGYp8KEOJdxB8lzkXNgtOQCYVYxGeZWBP_v-i-fW-QCfDhIDEcZqzInLw"

	return (
		<Card className="relative">
			<RecipeFavorite/>
			<CardHeader className="p-0 mb-2">
				<Image src={recipe.recipeImage} alt={recipe.name} className="rounded-t-md w-full select-none object-cover h-44" width={200} height={200}/>
			</CardHeader>
			<CardContent className="space-y-4">
				<CardTitle className="text-lg font-bold text-foreground">{recipe.name}</CardTitle>
				<div className="w-full text-muted-foreground flex *:flex-1 space-x-3">
					<RecipeTag>
						<Icons.rating className="h-5 w-5 text-yellow-500 fill-yellow-500"/>
						<p>{recipe.rating.toFixed(1)}</p>
					</RecipeTag>
					<RecipeTag>
						<Icons.time className="h-5 w-5" width={50}/>
						<p>{recipe.minutes.toFixed(0)}min</p>
					</RecipeTag>
					{recipe.diet && (
						<RecipeTag className="bg-green-200 text-lime-600 overflow-hidden whitespace-nowrap">
							<Icons.vegan className="h-5 w-5"/>
							<p className="w-14 truncate">{recipe.diet}</p>
						</RecipeTag>
					)}
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