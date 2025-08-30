import { BookOpen } from "lucide-react";
import React from "react";

const Header = () => {
  return (
    <header className="border-b border-border bg-card/50 backdrop-blur-sm sticky top-0 z-10">
      <div className="max-w-4xl mx-auto px-4 py-4">
        <div className="flex items-center gap-3">
          <div className="p-2 bg-primary rounded-lg">
            <BookOpen className="h-6 w-6 text-primary-foreground" />
          </div>
          <div>
            <h1 className="text-xl font-bold text-foreground">StudyBot AI</h1>
            <p className="text-sm text-muted-foreground">
              Your intelligent study companion
            </p>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
