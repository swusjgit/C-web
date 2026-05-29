import chapters from "@/data/chapters.json";

export interface Chapter {
  id: number;
  title: string;
  slug: string;
  content: string;
  difficulty: number;
  order: number;
  category_name: string;
  category_slug: string;
}

export interface ChapterSummary extends Omit<Chapter, "content"> {}

export interface ChapterGroup {
  slug: string;
  name: string;
  chapters: ChapterSummary[];
}

const CATEGORY_ORDER = ["basics", "cpp", "data-structure", "algorithm", "math"];

export const allChapters = chapters as Chapter[];

export const chapterSummaries: ChapterSummary[] = allChapters.map(({ content: _content, ...chapter }) => chapter);

export function getChapterBySlug(slug: string) {
  return allChapters.find((chapter) => chapter.slug === slug) ?? null;
}

export function getChapterGroups() {
  const map: Record<string, ChapterGroup> = {};

  for (const chapter of chapterSummaries) {
    if (!map[chapter.category_slug]) {
      map[chapter.category_slug] = {
        slug: chapter.category_slug,
        name: chapter.category_name,
        chapters: [],
      };
    }
    map[chapter.category_slug].chapters.push(chapter);
  }

  return CATEGORY_ORDER.filter((slug) => map[slug]).map((slug) => ({
    ...map[slug],
    chapters: [...map[slug].chapters].sort((a, b) => a.order - b.order),
  }));
}
