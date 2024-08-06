import { CircleDashed, UserCog } from "lucide-react";
import { Button } from "../../components/button";

export function Guests() {
  return (
    <div className="space-y-6">
      <h2 className="font-semibold text-xl">Convidados</h2>
      <div className="space-y-5">
        <div className="flex items-center justify-between gap-4">
          <div className="space-y-1.5 flex-1">
            <span className="font-medium text-zinc-100 block">
              Jessica White
            </span>
            <span className="text-sm text-zinc-400 block truncate">
              jessica.white44@yahoo.com
            </span>
          </div>
          <CircleDashed className="text-zinc-400 size-5" />
        </div>

        <div className="flex items-center justify-between gap-4">
          <div className="space-y-1.5 flex-1">
            <span className="font-medium text-zinc-100 block">
              Dr. Rita Pacocha
            </span>
            <span className="text-sm text-zinc-400 block truncate">
              lacy.stiedemann@gmail.com
            </span>
          </div>
          <CircleDashed className="text-zinc-400 size-5" />
        </div>
      </div>

      <Button variant="secondary" size="full">
        <UserCog className="size-5" />
        Gerenciar convidados
      </Button>
    </div>
  );
}
