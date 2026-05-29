import { allChapters, getChapterBySlug } from "@/lib/staticChapters";
import ChapterClient from "./ChapterClient";

export function generateStaticParams() {
  return allChapters.map((chapter) => ({ slug: chapter.slug }));
}

export default async function ChapterPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  return <ChapterClient chapter={getChapterBySlug(slug)} />;
}
