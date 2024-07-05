export type Recipe = {
	id: string;
	analyzedInstructions: [];
	cheap: boolean;
	cuisines: [];
	healthScore: number;
	image: string;
	ingredients: Ingredient[];
	instructions: string;
	readyInMinutes: number;
	servings: number;
	summary: string;
	title: string;
	equipment: string[];
	vegan: boolean;
	vegetarian: boolean;
};

export type Ingredient = {
	name: string;
	amount: number;
	unit: string;
};
