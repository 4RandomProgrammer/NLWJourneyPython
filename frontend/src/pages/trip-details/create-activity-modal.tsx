import { Calendar, Clock, Tag, X } from "lucide-react";
import { Button } from "../../components/button";

interface CreateActivityModalProps {
  closeCreateActivityModal: () => void;
}

export function CreateActivityModal({
  closeCreateActivityModal,
}: CreateActivityModalProps) {
  return (
    <div className="fixed inset-0 bg-black/60 flex items-center justify-center">
      <div className="w-[640px] rounded-xl py-5 px-6 shadow-shape bg-zinc-900 space-y-5">
        <div className="space-y-2">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-semibold">Cadastrar atividade</h2>
            <button type="button">
              <X
                onClick={closeCreateActivityModal}
                className="size-5 text-zinc-400"
              />
            </button>
          </div>
          <p className="text-sm text-zinc-400">
            Todos convidados podem visualizar as atividades.
          </p>
        </div>
        <div className="flex flex-wrap gap-2"></div>

        <form className="space-y-3">
          <div className="h-14 px-4 bg-zinc-950 border border-zinc-800 rounded-lg flex gap-2 items-center">
            <Tag className="text-zinc-400 size-5" />
            <input
              name="title"
              placeholder="Qual a atividade?"
              className="bg-transparent text-lg placeholder-zinc-400 outline-none flex-1"
            />
          </div>
          <div className="flex items gap-2">
            <div className="flex-1 h-14 p-4 bg-zinc-950 border border-zinc-800 rounded-lg flex gap-2">
              <Calendar className="text-zinc-400 size-5" />
              <input
                type="day"
                placeholder="20 de Agosto"
                className="bg-transparent text-lg placeholder-zinc-400 outline-none flex-1"
              />
            </div>
            <div className="w-36 h-14 p-4 bg-zinc-950 border border-zinc-800 rounded-lg flex gap-2">
              <Clock className="text-zinc-400 size-5" />
              <input
                name="occurs_at "
                type="text"
                placeholder="20 de Agosto"
                className="bg-transparent text-lg placeholder-zinc-400 outline-none flex-1"
              />
            </div>
          </div>
          <Button type="submit" variant="primary" size="full">
            Salvar atividade
          </Button>
        </form>
      </div>
    </div>
  );
}
