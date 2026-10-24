<!-- Source basis: the instructor's public repository https://github.com/iamshaunjp/laravel-11-for-beginners, using its lesson branch snapshots. These source snapshots are not a frame-by-frame transcription of the videos; video-only terminal commands and code that cannot be confirmed from the source are omitted. The repository has no `lesson-8` branch; its ninja migration below is placed in Lesson 8 based on the course sequence and first available snapshot (`lesson-9`). -->

### Lesson 1 — Laravel Tutorial for Beginners #1 - Introduction & Setup

**File:** `resources/views/welcome.blade.php`
```blade
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ninja Network</title>
</head>
<body>
  <h1>Welcome to the Ninja Network</h1>
  <p>Click the button below to view the list of ninjas.</p>
  
  <a href="" class="btn">
    Find Ninjas!
  </a>
</body>
</html>
```

**File:** `routes/web.php`
```php
<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});
```

### Lesson 2 — Laravel Tutorial for Beginners #2 - Routes & Views

**File:** `resources/views/ninjas/index.blade.php`
```blade
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ninja Network</title>
</head>
<body>
  <h2>Currently Available Ninjas</h2>
  
  <ul>
    <li>Ninjas here</li>
  </ul>
  
</body>
</html>
```

**File:** `resources/views/welcome.blade.php`
```blade
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ninja Network</title>
</head>
<body>
  <h1>Welcome to the Ninja Network</h1>
  <p>Click the button below to view the list of ninjas.</p>
  
  <a href="/ninjas" class="btn">
    Find Ninjas!
  </a>
</body>
</html>
```

**File:** `routes/web.php`
```php
<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/ninjas', function () {
  return view('ninjas.index');
});
```

### Lesson 3 — Laravel Tutorial for Beginners #3 - Route Wildcards & Data

**File:** `resources/views/ninjas/index.blade.php`
```blade
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ninja Network</title>
</head>
<body>
  <h2>Currently Available Ninjas</h2>
  <p>{{ $greeting }}</p>

  <ul>
    <li>
      <a href="/ninjas/{{ $ninjas[0]["id"] }}">
        {{ $ninjas[0]["name"] }}
      </a>
    </li>
    <li>
      <a href="/ninjas/{{ $ninjas[1]["id"] }}">
        {{ $ninjas[1]["name"] }}
      </a>
    </li>
  </ul>

</body>
</html>
```

**File:** `resources/views/ninjas/show.blade.php`
```blade
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ninja Network</title>
</head>
<body>
  <h2>Ninja id - {{ $id }}</h2>
</body>
</html>
```

**File:** `routes/web.php`
```php
<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/ninjas', function () {
  $ninjas = [
    ["name" => "mario","skill" => 75, "id" => "1"],
    ["name" => "luigi","skill" => 45, "id" => "2"],
  ];

  return view('ninjas.index', ["greeting" => "hello", "ninjas" => $ninjas]);
});

Route::get('/ninjas/{id}', function ($id) {
  // do something with the id
  // e.g. fetch a record from the db

  return view('ninjas.show', ['id' => $id]);
});
```

### Lesson 4 — Laravel Tutorial for Beginners #4 - Blade Directives

**File:** `resources/views/ninjas/index.blade.php`
```blade
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ninja Network</title>
</head>
<body>
  <h2>Currently Available Ninjas</h2>

  @if($greeting == 'hello')
    <p>Hi from inside the if statement</p>
  @endif

  <ul>
    @foreach($ninjas as $ninja)
      <li>
        <p>{{ $ninja['name'] }}</p>
        <a href="/ninjas/{{ $ninja['id'] }}">View Details</a>
      </li>
    @endforeach
  </ul>

</body>
</html>
```

### Lesson 5 — Laravel Tutorial for Beginners #5 - Layouts & Slots

**File:** `resources/views/components/layout.blade.php`
```blade
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ninja Network</title>
</head>
<body>

  <header>
    <nav>
      <h1>Ninja Network</h1>
      <a href="/ninjas"> 
        All Ninjas
      </a>
      <a href="/ninjas/create"> {{-- does not exit yet --}}
        Create New Ninja
      </a>
    </nav>
  </header>

  <main class="container">
    {{ $slot }}
  </main>

</body>
</html>
```

**File:** `resources/views/ninjas/create.blade.php`
```blade
<x-layout>
  <h2>Create Page</h2>
</x-layout>
```

**File:** `resources/views/ninjas/index.blade.php`
```blade
<x-layout>
  <h2>Currently Available Ninjas</h2>

  <ul>
    @foreach($ninjas as $ninja)
      <li>
        <p>{{ $ninja['name'] }}</p>
        <a href="/ninjas/{{ $ninja['id'] }}">View Details</a>
      </li>
    @endforeach
  </ul>
</x-layout>
```

**File:** `resources/views/ninjas/show.blade.php`
```blade
<x-layout>
  <h2>Ninja id - {{ $id }}</h2>
</x-layout>
```

**File:** `routes/web.php`
```php
<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/ninjas', function () {
  $ninjas = [
    ["name" => "mario","skill" => 75, "id" => "1"],
    ["name" => "luigi","skill" => 45, "id" => "2"],
  ];

  return view('ninjas.index', ["greeting" => "hello", "ninjas" => $ninjas]);
});

Route::get('/ninjas/create', function () {
  return view('ninjas.create');
});

Route::get('/ninjas/{id}', function ($id) {
  return view('ninjas.show', ['id' => $id]);
});
```

### Lesson 6 — Laravel Tutorial for Beginners #6 - Components, Attributes & Props

**File:** `resources/views/components/card.blade.php`
```blade
@props(['highlight' => false])

<div @class(['highlight' => $highlight, 'card']) >
  {{ $slot }}
  <a {{ $attributes }} class="btn">View Details</a>
</div>
```

**File:** `resources/views/components/layout.blade.php`
```blade
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ninja Network</title>
</head>
<body>

  <header>
    <nav>
      <h1>Ninja Network</h1>
      <a href="/ninjas"> 
        All Ninjas
      </a>
      <a href="/ninjas/create">
        Create New Ninja
      </a>
    </nav>
  </header>

  <main class="container">
    {{ $slot }}
  </main>

</body>
</html>
```

**File:** `resources/views/ninjas/index.blade.php`
```blade
<x-layout>
  <h2>Currently Available Ninjas</h2>

  <ul>
    @foreach($ninjas as $ninja)
      <li>
        <x-card :highlight="$ninja['skill'] > 70" href="/ninjas/{{$ninja['id']}}">
          <h3>{{ $ninja['name'] }}</h3>
        </x-card>
      </li>
    @endforeach
  </ul>
</x-layout>
```

**File:** `routes/web.php`
```php
<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/ninjas', function () {
  $ninjas = [
    ["name" => "mario","skill" => 75, "id" => "1"],
    ["name" => "luigi","skill" => 45, "id" => "2"],
  ];

  return view('ninjas.index', ["ninjas" => $ninjas]);
});

Route::get('/ninjas/create', function () {
  return view('ninjas.create');
});

Route::get('/ninjas/{id}', function ($id) {
  return view('ninjas.show', ['id' => $id]);
});
```

### Lesson 7 — Laravel Tutorial for Beginners #7 - Adding CSS & Tailwind

**File:** `package.json`
```json
{
    "private": true,
    "type": "module",
    "scripts": {
        "dev": "vite",
        "build": "vite build"
    },
    "devDependencies": {
        "autoprefixer": "^10.4.20",
        "axios": "^1.7.4",
        "laravel-vite-plugin": "^1.0",
        "postcss": "^8.4.47",
        "tailwindcss": "^3.4.13",
        "vite": "^5.0"
    }
}
```

**File:** `postcss.config.js`
```javascript
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```

**File:** `resources/css/app.css`
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
/* need PostCSS Language Support to remove warnings */

body {
  @apply bg-gray-100 text-gray-700;
  font-family: "Rubik";
}
h1 {
  @apply text-2xl font-bold text-red-500;
}
h2 {
  @apply text-xl font-bold my-4;
}
h3 {
  @apply text-lg font-bold my-4;
}
ul {
  @apply my-10;
}
p {
  @apply my-2;
}

/* header */
header {
  @apply bg-white;

  nav {
    @apply flex items-center gap-5 max-w-screen-lg px-12 py-4 mx-auto;
  }
  h1 {
    @apply mr-auto;
  }
}

/* form elements */
form {
  @apply max-w-screen-sm;
}
input, select, textarea {
  @apply block w-full mt-2 mb-4 p-2;
}

/* custom classes */
.container {
  @apply max-w-screen-lg mx-auto px-12 py-8;
}
.card {
  @apply bg-white rounded border border-gray-200 px-3 py-3 my-2 flex justify-between items-center;
}
.highlight {
  @apply border-l-4 border-l-red-500;
}
.btn {
  @apply rounded px-3 py-2 bg-gray-200 hover:bg-red-500 hover:text-white;
}
```

**File:** `resources/views/components/layout.blade.php`
```blade
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ninja Network</title>

  @vite('resources/css/app.css')
</head>
<body>

  <header>
    <nav>
      <h1>Ninja Network</h1>
      <a href="/ninjas"> 
        All Ninjas
      </a>
      <a href="/ninjas/create">
        Create New Ninja
      </a>
    </nav>
  </header>

  <main class="container">
    {{ $slot }}
  </main>

</body>
</html>
```

**File:** `resources/views/welcome.blade.php`
```blade
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ninja Network</title>

  @vite('resources/css/app.css')
</head>
<body class="text-center px-8 py-12">
  <h1>Welcome to the Ninja Network</h1>
  <p>Click the button below to view the list of ninjas.</p>
  
  <a href="/ninjas" class="btn mt-4 inline-block">
    Find Ninjas!
  </a>
</body>
</html>
```

**File:** `tailwind.config.js`
```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./resources/**/*.blade.php",
    "./resources/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

### Lesson 8 — Laravel Tutorial for Beginners #8 - Migrations

<!-- Reconstructed from the first available migration snapshot on lesson-9. -->

**File:** `database/migrations/2024_10_12_124138_create_ninjas_table.php`
```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('ninjas', function (Blueprint $table) {
            $table->id();
            $table->timestamps();
            $table->string('name');
            $table->integer('skill');
            $table->text('bio');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('ninjas');
    }
};
```

### Lesson 9 — Laravel Tutorial for Beginners #9 - Eloquent Models

**File:** `app/Models/Ninja.php`
```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Ninja extends Model
{
    protected $fillable = ['name', 'skill', 'bio'];

    /** @use HasFactory<\Database\Factories\NinjaFactory> */
    use HasFactory;
}
```

**File:** `database/factories/NinjaFactory.php`
```php
<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Ninja>
 */
class NinjaFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            //
        ];
    }
}
```

**File:** `database/seeders/NinjaSeeder.php`
```php
<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class NinjaSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        //
    }
}
```

### Lesson 10 — Laravel Tutorial for Beginners #10 - Model Factories

**File:** `database/factories/NinjaFactory.php`
```php
<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Ninja>
 */
class NinjaFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'name' => fake()->name(),
            'skill' => fake()->numberBetween(1, 100),
            'bio' =>fake()->realText(500),
        ];
    }
}
```

### Lesson 11 — Laravel Tutorial for Beginners #11 - Seeders

**File:** `database/seeders/DatabaseSeeder.php`
```php
<?php

namespace Database\Seeders;

use App\Models\User;
// use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     */
    public function run(): void
    {
        // User::factory(10)->create();

        User::factory()->create([
            'name' => 'Test User',
            'email' => 'test@example.com',
        ]);

        $this->call([
          NinjaSeeder::class,
        ]);
    }
}
```

**File:** `database/seeders/NinjaSeeder.php`
```php
<?php

namespace Database\Seeders;

use App\Models\Ninja;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class NinjaSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
      Ninja::factory()->count(50)->create();
    }
}
```

### Lesson 12 — Laravel Tutorial for Beginners #12 - MVC & Controllers

**File:** `app/Http/Controllers/NinjaController.php`
```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Ninja;

class NinjaController extends Controller
{
    public function index() {
      // route --> /ninjas/
      // fetch all records & pass into the index view

      // $ninjas = Ninja::all();
      $ninjas = Ninja::orderBy('created_at', 'desc')->get();

      return view('ninjas.index', ['ninjas' => $ninjas]);
    }

    public function show($id) {
      // route --> /ninjas/{id}
      // fetch a single record & pass into show view
    }

    public function create() {
      // route --> /ninjas/create
      // render a create view (with web form) to users
    }

    public function store() {
      // --> /ninjas/ (POST)
      // hanlde POST request to store a new ninja record in table
    }

    public function destroy($id) {
      // --> /ninjas/{id} (DELETE)
      // handle delete request to delete a ninja record from table
    }

    // edit() and update() for edit view and update requests
    // we won't be using these routes
}
```

**File:** `routes/web.php`
```php
<?php

use App\Http\Controllers\NinjaController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/ninjas', [NinjaController::class, 'index']);

Route::get('/ninjas/create', function () {
  return view('ninjas.create');
});

Route::get('/ninjas/{id}', function ($id) {
  return view('ninjas.show', ['id' => $id]);
});
```

### Lesson 13 — Laravel Tutorial for Beginners #13 - More on Controllers

**File:** `app/Http/Controllers/NinjaController.php`
```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Ninja;

class NinjaController extends Controller
{
    public function index() {
      // route --> /ninjas/
      // fetch all records & pass into the index view

      // $ninjas = Ninja::all();
      $ninjas = Ninja::orderBy('created_at', 'desc')->get();

      return view('ninjas.index', ['ninjas' => $ninjas]);
    }

    public function show($id) {
      // route --> /ninjas/{id}
      // fetch a single record & pass into show view
      $ninja = Ninja::findOrFail($id);

      return view('ninjas.show', ['ninja' => $ninja]);
    }

    public function create() {
      // route --> /ninjas/create
      // render a create view (with web form) to users
      return view('ninjas.create');
    }

    public function store() {
      // --> /ninjas/ (POST)
      // hanlde POST request to store a new ninja record in table
    }

    public function destroy($id) {
      // --> /ninjas/{id} (DELETE)
      // handle delete request to delete a ninja record from table
    }

    // edit() and update() for edit view and update requests
    // we won't be using these routes
}
```

**File:** `resources/views/ninjas/show.blade.php`
```blade
<x-layout>
  <h2>{{ $ninja->name }}'s Profile</h2>

  <div class="bg-gray-200 p-4 rounded">
    <p><strong>Skill level:</strong> {{ $ninja->skill }}</p>
    <p><strong>About me:</strong></p>
    <p>{{ $ninja->bio }}</p>
  </div>
</x-layout>
```

**File:** `routes/web.php`
```php
<?php

use App\Http\Controllers\NinjaController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/ninjas', [NinjaController::class, 'index']);
Route::get('/ninjas/create', [NinjaController::class, 'create']);
Route::get('/ninjas/{id}', [NinjaController::class, 'show']);
```

### Lesson 14 — Laravel Tutorial for Beginners #14 - Named Routes

**File:** `resources/views/components/layout.blade.php`
```blade
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ninja Network</title>

  @vite('resources/css/app.css')
</head>
<body>

  <header>
    <nav>
      <h1>Ninja Network</h1>
      <a href="{{ route('ninjas.index') }}"> 
        All Ninjas
      </a>
      <a href="{{ route('ninjas.create') }}">
        Create New Ninja
      </a>
    </nav>
  </header>

  <main class="container">
    {{ $slot }}
  </main>

</body>
</html>
```

**File:** `resources/views/ninjas/index.blade.php`
```blade
<x-layout>
  <h2>Currently Available Ninjas</h2>

  <ul>
    @foreach($ninjas as $ninja)
      <li>
        <x-card :highlight="$ninja['skill'] > 70" href="{{route('ninjas.show', $ninja->id)}}">
          <h3>{{ $ninja['name'] }}</h3>
        </x-card>
      </li>
    @endforeach
  </ul>
</x-layout>
```

**File:** `routes/web.php`
```php
<?php

use App\Http\Controllers\NinjaController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/ninjas', [NinjaController::class, 'index'])->name('ninjas.index');
Route::get('/ninjas/create', [NinjaController::class, 'create'])->name('ninjas.create');
Route::get('/ninjas/{id}', [NinjaController::class, 'show'])->name('ninjas.show');
```

### Lesson 15 — Laravel Tutorial for Beginners #15 - Pagination

**File:** `app/Http/Controllers/NinjaController.php`
```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Ninja;

class NinjaController extends Controller
{
    public function index() {
      // route --> /ninjas/
      // fetch all records & pass into the index view

      // $ninjas = Ninja::all();
      $ninjas = Ninja::orderBy('created_at', 'desc')->paginate(10);

      return view('ninjas.index', ['ninjas' => $ninjas]);
    }

    public function show($id) {
      // route --> /ninjas/{id}
      // fetch a single record & pass into show view
      $ninja = Ninja::findOrFail($id);

      return view('ninjas.show', ['ninja' => $ninja]);
    }

    public function create() {
      // route --> /ninjas/create
      // render a create view (with web form) to users
      return view('ninjas.create');
    }

    public function store() {
      // --> /ninjas/ (POST)
      // hanlde POST request to store a new ninja record in table
    }

    public function destroy($id) {
      // --> /ninjas/{id} (DELETE)
      // handle delete request to delete a ninja record from table
    }

    // edit() and update() for edit view and update requests
    // we won't be using these routes
}
```

**File:** `resources/views/ninjas/index.blade.php`
```blade
<x-layout>
  <h2>Currently Available Ninjas</h2>

  <ul>
    @foreach($ninjas as $ninja)
      <li>
        <x-card :highlight="$ninja['skill'] > 70" href="{{route('ninjas.show', $ninja->id)}}">
          <h3>{{ $ninja['name'] }}</h3>
        </x-card>
      </li>
    @endforeach
  </ul>

  {{ $ninjas->links() }}
</x-layout>
```

**File:** `resources/views/vendor/pagination/bootstrap-4.blade.php`
```blade
@if ($paginator->hasPages())
    <nav>
        <ul class="pagination">
            {{-- Previous Page Link --}}
            @if ($paginator->onFirstPage())
                <li class="page-item disabled" aria-disabled="true" aria-label="@lang('pagination.previous')">
                    <span class="page-link" aria-hidden="true">&lsaquo;</span>
                </li>
            @else
                <li class="page-item">
                    <a class="page-link" href="{{ $paginator->previousPageUrl() }}" rel="prev" aria-label="@lang('pagination.previous')">&lsaquo;</a>
                </li>
            @endif

            {{-- Pagination Elements --}}
            @foreach ($elements as $element)
                {{-- "Three Dots" Separator --}}
                @if (is_string($element))
                    <li class="page-item disabled" aria-disabled="true"><span class="page-link">{{ $element }}</span></li>
                @endif

                {{-- Array Of Links --}}
                @if (is_array($element))
                    @foreach ($element as $page => $url)
                        @if ($page == $paginator->currentPage())
                            <li class="page-item active" aria-current="page"><span class="page-link">{{ $page }}</span></li>
                        @else
                            <li class="page-item"><a class="page-link" href="{{ $url }}">{{ $page }}</a></li>
                        @endif
                    @endforeach
                @endif
            @endforeach

            {{-- Next Page Link --}}
            @if ($paginator->hasMorePages())
                <li class="page-item">
                    <a class="page-link" href="{{ $paginator->nextPageUrl() }}" rel="next" aria-label="@lang('pagination.next')">&rsaquo;</a>
                </li>
            @else
                <li class="page-item disabled" aria-disabled="true" aria-label="@lang('pagination.next')">
                    <span class="page-link" aria-hidden="true">&rsaquo;</span>
                </li>
            @endif
        </ul>
    </nav>
@endif
```

**File:** `resources/views/vendor/pagination/bootstrap-5.blade.php`
```blade
@if ($paginator->hasPages())
    <nav class="d-flex justify-items-center justify-content-between">
        <div class="d-flex justify-content-between flex-fill d-sm-none">
            <ul class="pagination">
                {{-- Previous Page Link --}}
                @if ($paginator->onFirstPage())
                    <li class="page-item disabled" aria-disabled="true">
                        <span class="page-link">@lang('pagination.previous')</span>
                    </li>
                @else
                    <li class="page-item">
                        <a class="page-link" href="{{ $paginator->previousPageUrl() }}" rel="prev">@lang('pagination.previous')</a>
                    </li>
                @endif

                {{-- Next Page Link --}}
                @if ($paginator->hasMorePages())
                    <li class="page-item">
                        <a class="page-link" href="{{ $paginator->nextPageUrl() }}" rel="next">@lang('pagination.next')</a>
                    </li>
                @else
                    <li class="page-item disabled" aria-disabled="true">
                        <span class="page-link">@lang('pagination.next')</span>
                    </li>
                @endif
            </ul>
        </div>

        <div class="d-none flex-sm-fill d-sm-flex align-items-sm-center justify-content-sm-between">
            <div>
                <p class="small text-muted">
                    {!! __('Showing') !!}
                    <span class="fw-semibold">{{ $paginator->firstItem() }}</span>
                    {!! __('to') !!}
                    <span class="fw-semibold">{{ $paginator->lastItem() }}</span>
                    {!! __('of') !!}
                    <span class="fw-semibold">{{ $paginator->total() }}</span>
                    {!! __('results') !!}
                </p>
            </div>

            <div>
                <ul class="pagination">
                    {{-- Previous Page Link --}}
                    @if ($paginator->onFirstPage())
                        <li class="page-item disabled" aria-disabled="true" aria-label="@lang('pagination.previous')">
                            <span class="page-link" aria-hidden="true">&lsaquo;</span>
                        </li>
                    @else
                        <li class="page-item">
                            <a class="page-link" href="{{ $paginator->previousPageUrl() }}" rel="prev" aria-label="@lang('pagination.previous')">&lsaquo;</a>
                        </li>
                    @endif

                    {{-- Pagination Elements --}}
                    @foreach ($elements as $element)
                        {{-- "Three Dots" Separator --}}
                        @if (is_string($element))
                            <li class="page-item disabled" aria-disabled="true"><span class="page-link">{{ $element }}</span></li>
                        @endif

                        {{-- Array Of Links --}}
                        @if (is_array($element))
                            @foreach ($element as $page => $url)
                                @if ($page == $paginator->currentPage())
                                    <li class="page-item active" aria-current="page"><span class="page-link">{{ $page }}</span></li>
                                @else
                                    <li class="page-item"><a class="page-link" href="{{ $url }}">{{ $page }}</a></li>
                                @endif
                            @endforeach
                        @endif
                    @endforeach

                    {{-- Next Page Link --}}
                    @if ($paginator->hasMorePages())
                        <li class="page-item">
                            <a class="page-link" href="{{ $paginator->nextPageUrl() }}" rel="next" aria-label="@lang('pagination.next')">&rsaquo;</a>
                        </li>
                    @else
                        <li class="page-item disabled" aria-disabled="true" aria-label="@lang('pagination.next')">
                            <span class="page-link" aria-hidden="true">&rsaquo;</span>
                        </li>
                    @endif
                </ul>
            </div>
        </div>
    </nav>
@endif
```

**File:** `resources/views/vendor/pagination/default.blade.php`
```blade
@if ($paginator->hasPages())
    <nav>
        <ul class="pagination">
            {{-- Previous Page Link --}}
            @if ($paginator->onFirstPage())
                <li class="disabled" aria-disabled="true" aria-label="@lang('pagination.previous')">
                    <span aria-hidden="true">&lsaquo;</span>
                </li>
            @else
                <li>
                    <a href="{{ $paginator->previousPageUrl() }}" rel="prev" aria-label="@lang('pagination.previous')">&lsaquo;</a>
                </li>
            @endif

            {{-- Pagination Elements --}}
            @foreach ($elements as $element)
                {{-- "Three Dots" Separator --}}
                @if (is_string($element))
                    <li class="disabled" aria-disabled="true"><span>{{ $element }}</span></li>
                @endif

                {{-- Array Of Links --}}
                @if (is_array($element))
                    @foreach ($element as $page => $url)
                        @if ($page == $paginator->currentPage())
                            <li class="active" aria-current="page"><span>{{ $page }}</span></li>
                        @else
                            <li><a href="{{ $url }}">{{ $page }}</a></li>
                        @endif
                    @endforeach
                @endif
            @endforeach

            {{-- Next Page Link --}}
            @if ($paginator->hasMorePages())
                <li>
                    <a href="{{ $paginator->nextPageUrl() }}" rel="next" aria-label="@lang('pagination.next')">&rsaquo;</a>
                </li>
            @else
                <li class="disabled" aria-disabled="true" aria-label="@lang('pagination.next')">
                    <span aria-hidden="true">&rsaquo;</span>
                </li>
            @endif
        </ul>
    </nav>
@endif
```

**File:** `resources/views/vendor/pagination/semantic-ui.blade.php`
```blade
@if ($paginator->hasPages())
    <div class="ui pagination menu" role="navigation">
        {{-- Previous Page Link --}}
        @if ($paginator->onFirstPage())
            <a class="icon item disabled" aria-disabled="true" aria-label="@lang('pagination.previous')"> <i class="left chevron icon"></i> </a>
        @else
            <a class="icon item" href="{{ $paginator->previousPageUrl() }}" rel="prev" aria-label="@lang('pagination.previous')"> <i class="left chevron icon"></i> </a>
        @endif

        {{-- Pagination Elements --}}
        @foreach ($elements as $element)
            {{-- "Three Dots" Separator --}}
            @if (is_string($element))
                <a class="icon item disabled" aria-disabled="true">{{ $element }}</a>
            @endif

            {{-- Array Of Links --}}
            @if (is_array($element))
                @foreach ($element as $page => $url)
                    @if ($page == $paginator->currentPage())
                        <a class="item active" href="{{ $url }}" aria-current="page">{{ $page }}</a>
                    @else
                        <a class="item" href="{{ $url }}">{{ $page }}</a>
                    @endif
                @endforeach
            @endif
        @endforeach

        {{-- Next Page Link --}}
        @if ($paginator->hasMorePages())
            <a class="icon item" href="{{ $paginator->nextPageUrl() }}" rel="next" aria-label="@lang('pagination.next')"> <i class="right chevron icon"></i> </a>
        @else
            <a class="icon item disabled" aria-disabled="true" aria-label="@lang('pagination.next')"> <i class="right chevron icon"></i> </a>
        @endif
    </div>
@endif
```

**File:** `resources/views/vendor/pagination/simple-bootstrap-4.blade.php`
```blade
@if ($paginator->hasPages())
    <nav>
        <ul class="pagination">
            {{-- Previous Page Link --}}
            @if ($paginator->onFirstPage())
                <li class="page-item disabled" aria-disabled="true">
                    <span class="page-link">@lang('pagination.previous')</span>
                </li>
            @else
                <li class="page-item">
                    <a class="page-link" href="{{ $paginator->previousPageUrl() }}" rel="prev">@lang('pagination.previous')</a>
                </li>
            @endif

            {{-- Next Page Link --}}
            @if ($paginator->hasMorePages())
                <li class="page-item">
                    <a class="page-link" href="{{ $paginator->nextPageUrl() }}" rel="next">@lang('pagination.next')</a>
                </li>
            @else
                <li class="page-item disabled" aria-disabled="true">
                    <span class="page-link">@lang('pagination.next')</span>
                </li>
            @endif
        </ul>
    </nav>
@endif
```

**File:** `resources/views/vendor/pagination/simple-bootstrap-5.blade.php`
```blade
@if ($paginator->hasPages())
    <nav role="navigation" aria-label="Pagination Navigation">
        <ul class="pagination">
            {{-- Previous Page Link --}}
            @if ($paginator->onFirstPage())
                <li class="page-item disabled" aria-disabled="true">
                    <span class="page-link">{!! __('pagination.previous') !!}</span>
                </li>
            @else
                <li class="page-item">
                    <a class="page-link" href="{{ $paginator->previousPageUrl() }}" rel="prev">
                        {!! __('pagination.previous') !!}
                    </a>
                </li>
            @endif

            {{-- Next Page Link --}}
            @if ($paginator->hasMorePages())
                <li class="page-item">
                    <a class="page-link" href="{{ $paginator->nextPageUrl() }}" rel="next">{!! __('pagination.next') !!}</a>
                </li>
            @else
                <li class="page-item disabled" aria-disabled="true">
                    <span class="page-link">{!! __('pagination.next') !!}</span>
                </li>
            @endif
        </ul>
    </nav>
@endif
```

**File:** `resources/views/vendor/pagination/simple-default.blade.php`
```blade
@if ($paginator->hasPages())
    <nav>
        <ul class="pagination">
            {{-- Previous Page Link --}}
            @if ($paginator->onFirstPage())
                <li class="disabled" aria-disabled="true"><span>@lang('pagination.previous')</span></li>
            @else
                <li><a href="{{ $paginator->previousPageUrl() }}" rel="prev">@lang('pagination.previous')</a></li>
            @endif

            {{-- Next Page Link --}}
            @if ($paginator->hasMorePages())
                <li><a href="{{ $paginator->nextPageUrl() }}" rel="next">@lang('pagination.next')</a></li>
            @else
                <li class="disabled" aria-disabled="true"><span>@lang('pagination.next')</span></li>
            @endif
        </ul>
    </nav>
@endif
```

**File:** `resources/views/vendor/pagination/simple-tailwind.blade.php`
```blade
@if ($paginator->hasPages())
    <nav role="navigation" aria-label="Pagination Navigation" class="flex justify-between">
        {{-- Previous Page Link --}}
        @if ($paginator->onFirstPage())
            <span class="relative inline-flex items-center px-4 py-2 text-sm font-medium text-gray-500 bg-white border border-gray-300 cursor-default leading-5 rounded-md dark:text-gray-600 dark:bg-gray-800 dark:border-gray-600">
                {!! __('pagination.previous') !!}
            </span>
        @else
            <a href="{{ $paginator->previousPageUrl() }}" rel="prev" class="relative inline-flex items-center px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 leading-5 rounded-md hover:text-gray-500 focus:outline-none focus:ring ring-gray-300 focus:border-blue-300 active:bg-gray-100 active:text-gray-700 transition ease-in-out duration-150 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-300 dark:focus:border-blue-700 dark:active:bg-gray-700 dark:active:text-gray-300">
                {!! __('pagination.previous') !!}
            </a>
        @endif

        {{-- Next Page Link --}}
        @if ($paginator->hasMorePages())
            <a href="{{ $paginator->nextPageUrl() }}" rel="next" class="relative inline-flex items-center px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 leading-5 rounded-md hover:text-gray-500 focus:outline-none focus:ring ring-gray-300 focus:border-blue-300 active:bg-gray-100 active:text-gray-700 transition ease-in-out duration-150 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-300 dark:focus:border-blue-700 dark:active:bg-gray-700 dark:active:text-gray-300">
                {!! __('pagination.next') !!}
            </a>
        @else
            <span class="relative inline-flex items-center px-4 py-2 text-sm font-medium text-gray-500 bg-white border border-gray-300 cursor-default leading-5 rounded-md dark:text-gray-600 dark:bg-gray-800 dark:border-gray-600">
                {!! __('pagination.next') !!}
            </span>
        @endif
    </nav>
@endif
```

**File:** `resources/views/vendor/pagination/tailwind.blade.php`
```blade
@if ($paginator->hasPages())
    <nav role="navigation" aria-label="{{ __('Pagination Navigation') }}" class="flex items-center justify-between">
        <div class="flex justify-between flex-1 sm:hidden">
            @if ($paginator->onFirstPage())
                <span class="relative inline-flex items-center px-4 py-2 text-sm font-medium text-gray-500 bg-white border border-gray-300 cursor-default leading-5 rounded-md dark:text-gray-600 dark:bg-gray-800 dark:border-gray-600">
                    {!! __('pagination.previous') !!}
                </span>
            @else
                <a href="{{ $paginator->previousPageUrl() }}" class="relative inline-flex items-center px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 leading-5 rounded-md hover:text-gray-500 focus:outline-none focus:ring ring-gray-300 focus:border-blue-300 active:bg-gray-100 active:text-gray-700 transition ease-in-out duration-150 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-300 dark:focus:border-blue-700 dark:active:bg-gray-700 dark:active:text-gray-300">
                    {!! __('pagination.previous') !!}
                </a>
            @endif

            @if ($paginator->hasMorePages())
                <a href="{{ $paginator->nextPageUrl() }}" class="relative inline-flex items-center px-4 py-2 ml-3 text-sm font-medium text-gray-700 bg-white border border-gray-300 leading-5 rounded-md hover:text-gray-500 focus:outline-none focus:ring ring-gray-300 focus:border-blue-300 active:bg-gray-100 active:text-gray-700 transition ease-in-out duration-150 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-300 dark:focus:border-blue-700 dark:active:bg-gray-700 dark:active:text-gray-300">
                    {!! __('pagination.next') !!}
                </a>
            @else
                <span class="relative inline-flex items-center px-4 py-2 ml-3 text-sm font-medium text-gray-500 bg-white border border-gray-300 cursor-default leading-5 rounded-md dark:text-gray-600 dark:bg-gray-800 dark:border-gray-600">
                    {!! __('pagination.next') !!}
                </span>
            @endif
        </div>

        <div class="hidden sm:flex-1 sm:flex sm:items-center sm:justify-between">
            <div>
                <p class="text-sm text-gray-700 leading-5 dark:text-gray-400">
                    {!! __('Showing') !!}
                    @if ($paginator->firstItem())
                        <span class="font-medium">{{ $paginator->firstItem() }}</span>
                        {!! __('to') !!}
                        <span class="font-medium">{{ $paginator->lastItem() }}</span>
                    @else
                        {{ $paginator->count() }}
                    @endif
                    {!! __('of') !!}
                    <span class="font-medium">{{ $paginator->total() }}</span>
                    {!! __('results') !!}
                </p>
            </div>

            <div>
                <span class="relative z-0 inline-flex rtl:flex-row-reverse shadow-sm rounded-md">
                    {{-- Previous Page Link --}}
                    @if ($paginator->onFirstPage())
                        <span aria-disabled="true" aria-label="{{ __('pagination.previous') }}">
                            <span class="relative inline-flex items-center px-2 py-2 text-sm font-medium text-gray-500 bg-white border border-gray-300 cursor-default rounded-l-md leading-5 dark:bg-gray-800 dark:border-gray-600" aria-hidden="true">
                                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                                    <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
                                </svg>
                            </span>
                        </span>
                    @else
                        <a href="{{ $paginator->previousPageUrl() }}" rel="prev" class="relative inline-flex items-center px-2 py-2 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-l-md leading-5 hover:text-gray-400 focus:z-10 focus:outline-none focus:ring ring-gray-300 focus:border-blue-300 active:bg-gray-100 active:text-gray-500 transition ease-in-out duration-150 dark:bg-gray-800 dark:border-gray-600 dark:active:bg-gray-700 dark:focus:border-blue-800" aria-label="{{ __('pagination.previous') }}">
                            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
                            </svg>
                        </a>
                    @endif

                    {{-- Pagination Elements --}}
                    @foreach ($elements as $element)
                        {{-- "Three Dots" Separator --}}
                        @if (is_string($element))
                            <span aria-disabled="true">
                                <span class="relative inline-flex items-center px-4 py-2 -ml-px text-sm font-medium text-gray-700 bg-white border border-gray-300 cursor-default leading-5 dark:bg-gray-800 dark:border-gray-600">{{ $element }}</span>
                            </span>
                        @endif

                        {{-- Array Of Links --}}
                        @if (is_array($element))
                            @foreach ($element as $page => $url)
                                @if ($page == $paginator->currentPage())
                                    <span aria-current="page">
                                        <span class="relative inline-flex items-center px-4 py-2 -ml-px text-sm font-medium text-gray-500 bg-white border border-gray-300 cursor-default leading-5 dark:bg-gray-800 dark:border-gray-600">{{ $page }}</span>
                                    </span>
                                @else
                                    <a href="{{ $url }}" class="relative inline-flex items-center px-4 py-2 -ml-px text-sm font-medium text-gray-700 bg-white border border-gray-300 leading-5 hover:text-gray-500 focus:z-10 focus:outline-none focus:ring ring-gray-300 focus:border-blue-300 active:bg-gray-100 active:text-gray-700 transition ease-in-out duration-150 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-400 dark:hover:text-gray-300 dark:active:bg-gray-700 dark:focus:border-blue-800" aria-label="{{ __('Go to page :page', ['page' => $page]) }}">
                                        {{ $page }}
                                    </a>
                                @endif
                            @endforeach
                        @endif
                    @endforeach

                    {{-- Next Page Link --}}
                    @if ($paginator->hasMorePages())
                        <a href="{{ $paginator->nextPageUrl() }}" rel="next" class="relative inline-flex items-center px-2 py-2 -ml-px text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-r-md leading-5 hover:text-gray-400 focus:z-10 focus:outline-none focus:ring ring-gray-300 focus:border-blue-300 active:bg-gray-100 active:text-gray-500 transition ease-in-out duration-150 dark:bg-gray-800 dark:border-gray-600 dark:active:bg-gray-700 dark:focus:border-blue-800" aria-label="{{ __('pagination.next') }}">
                            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                            </svg>
                        </a>
                    @else
                        <span aria-disabled="true" aria-label="{{ __('pagination.next') }}">
                            <span class="relative inline-flex items-center px-2 py-2 -ml-px text-sm font-medium text-gray-500 bg-white border border-gray-300 cursor-default rounded-r-md leading-5 dark:bg-gray-800 dark:border-gray-600" aria-hidden="true">
                                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                                    <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                                </svg>
                            </span>
                        </span>
                    @endif
                </span>
            </div>
        </div>
    </nav>
@endif
```

### Lesson 16 — Laravel Tutorial for Beginners #16 - Foreign Keys (part 1)

**File:** `app/Models/Dojo.php`
```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Dojo extends Model
{
    /** @use HasFactory<\Database\Factories\DojoFactory> */
    use HasFactory;

    protected $fillable = ['name', 'location', 'description'];
}
```

**File:** `composer.json`
```json
{
    "name": "laravel/laravel",
    "type": "project",
    "description": "The skeleton application for the Laravel framework.",
    "keywords": ["laravel", "framework"],
    "license": "MIT",
    "require": {
        "php": "^8.2",
        "laravel/framework": "^11.9",
        "laravel/tinker": "^2.9"
    },
    "require-dev": {
        "barryvdh/laravel-debugbar": "^3.14",
        "fakerphp/faker": "^1.23",
        "laravel/pint": "^1.13",
        "laravel/sail": "^1.26",
        "mockery/mockery": "^1.6",
        "nunomaduro/collision": "^8.0",
        "pestphp/pest": "^3.3",
        "pestphp/pest-plugin-laravel": "^3.0"
    },
    "autoload": {
        "psr-4": {
            "App\\": "app/",
            "Database\\Factories\\": "database/factories/",
            "Database\\Seeders\\": "database/seeders/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "Tests\\": "tests/"
        }
    },
    "scripts": {
        "post-autoload-dump": [
            "Illuminate\\Foundation\\ComposerScripts::postAutoloadDump",
            "@php artisan package:discover --ansi"
        ],
        "post-update-cmd": [
            "@php artisan vendor:publish --tag=laravel-assets --ansi --force"
        ],
        "post-root-package-install": [
            "@php -r \"file_exists('.env') || copy('.env.example', '.env');\""
        ],
        "post-create-project-cmd": [
            "@php artisan key:generate --ansi",
            "@php -r \"file_exists('database/database.sqlite') || touch('database/database.sqlite');\"",
            "@php artisan migrate --graceful --ansi"
        ]
    },
    "extra": {
        "laravel": {
            "dont-discover": []
        }
    },
    "config": {
        "optimize-autoloader": true,
        "preferred-install": "dist",
        "sort-packages": true,
        "allow-plugins": {
            "pestphp/pest-plugin": true,
            "php-http/discovery": true
        }
    },
    "minimum-stability": "stable",
    "prefer-stable": true
}
```

**File:** `database/factories/DojoFactory.php`
```php
<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Dojo>
 */
class DojoFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'name' => fake()->company(),
            'location' => fake()->city(),
            'description' => fake()->paragraph(10)
        ];
    }
}
```

**File:** `database/factories/NinjaFactory.php`
```php
<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use App\Models\Dojo;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Ninja>
 */
class NinjaFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'name' => fake()->name(),
            'skill' => fake()->numberBetween(1, 100),
            'bio' =>fake()->realText(500),
            'dojo_id' => Dojo::inRandomOrder()->first()->id,
        ];
    }
}
```

**File:** `database/migrations/2024_10_12_124138_create_ninjas_table.php`
```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('ninjas', function (Blueprint $table) {
            $table->id();
            $table->timestamps();
            $table->string('name');
            $table->integer('skill');
            $table->text('bio');
            $table->foreignId('dojo_id')->constrained()->onDelete('cascade');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('ninjas');
    }
};
```

**File:** `database/migrations/2024_10_14_123704_create_dojos_table.php`
```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('dojos', function (Blueprint $table) {
            $table->id();
            $table->timestamps();
            $table->string('name');
            $table->text('description');
            $table->string('location');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('dojos');
    }
};
```

**File:** `database/seeders/DatabaseSeeder.php`
```php
<?php

namespace Database\Seeders;

use App\Models\User;
// use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     */
    public function run(): void
    {
        // User::factory(10)->create();

        User::factory()->create([
            'name' => 'Test User',
            'email' => 'test@example.com',
        ]);

        $this->call([
          DojoSeeder::class,
        ]);

        $this->call([
          NinjaSeeder::class,
        ]);
    }
}
```

**File:** `database/seeders/DojoSeeder.php`
```php
<?php

namespace Database\Seeders;

use App\Models\Dojo;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class DojoSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
      Dojo::factory()->count(10)->create();
    }
}
```

**File:** `resources/views/ninjas/show.blade.php`
```blade
<x-layout>
  <h2>{{ $ninja->name }}'s Profile</h2>

  {{-- ninja info --}}
  <div class="bg-gray-200 p-4 rounded">
    <p><strong>Skill level:</strong> {{ $ninja->skill }}</p>
    <p><strong>About me:</strong></p>
    <p>{{ $ninja->bio }}</p>
  </div>

</x-layout>
```

**File:** `routes/web.php`
```php
<?php

use App\Http\Controllers\NinjaController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/ninjas', [NinjaController::class, 'index'])->name('ninjas.index');
Route::get('/ninjas/create', [NinjaController::class, 'create'])->name('ninjas.create');
Route::get('/ninjas/{id}', [NinjaController::class, 'show'])->name('ninjas.show');


/*

  new resource -> Dojo(s)
    - name, description, location

  each ninja belongs to a single dojo

  Ninja table
  ---------------------------------
  id | name | bio | skill | dojo_id
  ---------------------------------
  01 | jack | ... | 59    | 03
  02 | jill | ... | 85    | 01
  03 | sian | ... | 40    | 03
  04 | brad | ... | 70    | 02
  05 | lars | ... | 99    | 01
  06 | anne | ... | 55    | 01
  ---------------------------------

  Dojo table
  ----------------------------------
  id | name | description | location
  ----------------------------------
  01 | gold | ...         | uk
  02 | abc  | ...         | germany
  03 | hwah | ...         | india

*/
```

### Lesson 17 — Laravel Tutorial for Beginners #17 - Foreign Keys (part 2)

**File:** `app/Http/Controllers/NinjaController.php`
```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Ninja;

class NinjaController extends Controller
{
    public function index() {
      // route --> /ninjas/
      $ninjas = Ninja::with('dojo')->orderBy('created_at', 'desc')->paginate(10);

      return view('ninjas.index', ['ninjas' => $ninjas]);
    }

    public function show($id) {
      // route --> /ninjas/{id}
      $ninja = Ninja::with('dojo')->findOrFail($id);

      return view('ninjas.show', ['ninja' => $ninja]);
    }

    public function create() {
      // route --> /ninjas/create
      return view('ninjas.create');
    }

    public function store() {
      // --> /ninjas/ (POST)
      // hanlde POST request to store a new ninja record in table
    }

    public function destroy($id) {
      // --> /ninjas/{id} (DELETE)
      // handle delete request to delete a ninja record from table
    }

    // edit() and update() for edit view and update requests
    // we won't be using these routes
}
```

**File:** `app/Models/Dojo.php`
```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Dojo extends Model
{
    /** @use HasFactory<\Database\Factories\DojoFactory> */
    use HasFactory;

    protected $fillable = ['name', 'location', 'description'];

    public function ninjas()
    {
        return $this->hasMany(Ninja::class);
    }
}
```

**File:** `app/Models/Ninja.php`
```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Ninja extends Model
{
    protected $fillable = ['name', 'skill', 'bio'];

    /** @use HasFactory<\Database\Factories\NinjaFactory> */
    use HasFactory;

    public function dojo()
    {
        return $this->belongsTo(Dojo::class);
    }
}
```

**File:** `resources/views/ninjas/index.blade.php`
```blade
<x-layout>
  <h2>Currently Available Ninjas</h2>

  <ul>
    @foreach($ninjas as $ninja)
      <li>
        <x-card :highlight="$ninja['skill'] > 70" href="{{route('ninjas.show', $ninja->id)}}">
          <div>
            <h3>{{ $ninja->name }}</h3>
            <p>{{ $ninja->dojo->name }}</p>
          </div>
        </x-card>
      </li>
    @endforeach
  </ul>

  {{ $ninjas->links() }}
</x-layout>
```

**File:** `resources/views/ninjas/show.blade.php`
```blade
<x-layout>
  <h2>{{ $ninja->name }}'s Profile</h2>

  {{-- ninja info --}}
  <div class="bg-gray-200 p-4 rounded">
    <p><strong>Skill level:</strong> {{ $ninja->skill }}</p>
    <p><strong>About me:</strong></p>
    <p>{{ $ninja->bio }}</p>
  </div>

  {{-- dojo info --}}
  <div class="border-2 border-dashed bg-white px-4 pb-4 my-4 rounded">
    <h3>Dojo Information</h3>
    <p><strong>Dojo name:</strong> {{ $ninja->dojo->name }}</p>
    <p><strong>Location:</strong> {{ $ninja->dojo->location }}</p>
    <p><strong>About the Dojo:</strong></p>
    <p>{{ $ninja->dojo->description }}</p>
  </div>

</x-layout>
```

### Lesson 18 — Laravel Tutorial for Beginners #18 - Making a Web Form

**File:** `_templates/web_form.blade.php`
```blade
<form action="" method="">
  <h2>Create a New Ninja</h2>

  <!-- ninja Name -->
  <label for="name">Ninja Name:</label>
  <input 
    type="text" 
    id="name" 
    name="name" 
    value="{{ old('name') }}" 
    required
  >

  <!-- ninja Strength -->
  <label for="skill">Ninja Skill (0-100):</label>
  <input 
    type="number" 
    id="skill" 
    name="skill" 
    required
  >

  <!-- ninja Bio -->
  <label for="bio">Biography:</label>
  <textarea
    rows="5"
    id="bio" 
    name="bio" 
    required
  ></textarea>

  <!-- select a dojo -->
  <label for="dojo_id">Dojo:</label>
  <select id="dojo_id" name="dojo_id" required>
    <option value="" disabled selected>Select a dojo</option>
    
  </select>

  <button type="submit" class="btn mt-4">Create Ninja</button>

  <!-- validation errors -->
  
</form>
```

**File:** `app/Http/Controllers/NinjaController.php`
```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Ninja;
use App\Models\Dojo;

class NinjaController extends Controller
{
    public function index() {
      // route --> /ninjas/
      $ninjas = Ninja::with('dojo')->orderBy('created_at', 'desc')->paginate(10);

      return view('ninjas.index', ['ninjas' => $ninjas]);
    }

    public function show($id) {
      // route --> /ninjas/{id}
      $ninja = Ninja::with('dojo')->findOrFail($id);

      return view('ninjas.show', ['ninja' => $ninja]);
    }

    public function create() {
      // route --> /ninjas/create
      $dojos = Dojo::all();

      return view('ninjas.create', ['dojos' => $dojos]);
    }

    public function store() {
      // --> /ninjas/ (POST)
      // hanlde POST request to store a new ninja record in table
    }

    public function destroy($id) {
      // --> /ninjas/{id} (DELETE)
      // handle delete request to delete a ninja record from table
    }

    // edit() and update() for edit view and update requests
    // we won't be using these routes
}
```

**File:** `resources/views/ninjas/create.blade.php`
```blade
<x-layout>
  <form action="" method="">
    <!-- CSRF token for security -->
    @csrf

    <h2>Create a New Ninja</h2>

    <!-- ninja Name -->
    <label for="name">Ninja Name:</label>
    <input 
      type="text" 
      id="name" 
      name="name" 
      required
    >

    <!-- ninja Strength -->
    <label for="skill">Ninja Skill (0-100):</label>
    <input 
      type="number" 
      id="skill" 
      name="skill" 
      required
    >

    <!-- ninja Bio -->
    <label for="bio">Biography:</label>
    <textarea
      rows="5"
      id="bio" 
      name="bio" 
      required
    ></textarea>

    <!-- select a dojo -->
    <label for="dojo_id">Dojo:</label>
    <select id="dojo_id" name="dojo_id" required>
      <option value="" disabled selected>Select a dojo</option>
      @foreach ($dojos as $dojo)
        <option value="{{ $dojo->id }}">
          {{ $dojo->name }}
        </option>
      @endforeach
    </select>

    <button type="submit" class="btn mt-4">Create Ninja</button>

    <!-- validation errors -->
    
  </form>
</x-layout>
```

### Lesson 19 — Laravel Tutorial for Beginners #19 - Handling POST Requests

**File:** `app/Http/Controllers/NinjaController.php`
```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Ninja;
use App\Models\Dojo;

class NinjaController extends Controller
{
    public function index() {
      // route --> /ninjas/
      $ninjas = Ninja::with('dojo')->orderBy('created_at', 'desc')->paginate(10);

      return view('ninjas.index', ['ninjas' => $ninjas]);
    }

    public function show($id) {
      // route --> /ninjas/{id}
      $ninja = Ninja::with('dojo')->findOrFail($id);

      return view('ninjas.show', ['ninja' => $ninja]);
    }

    public function create() {
      // route --> /ninjas/create
      $dojos = Dojo::all();

      return view('ninjas.create', ['dojos' => $dojos]);
    }

    public function store(Request $request) {
      // --> /ninjas/ (POST)
      $validated = $request->validate([
        'name' => 'required|string|max:255',
        'skill' => 'required|integer|min:0|max:100',
        'bio' => 'required|string|min:20|max:1000',
        'dojo_id' => 'required|exists:dojos,id',
      ]);

      Ninja::create($validated);

      return redirect()->route('ninjas.index');
    }

    public function destroy($id) {
      // --> /ninjas/{id} (DELETE)
      // handle delete request to delete a ninja record from table
    }

    // edit() and update() for edit view and update requests
    // we won't be using these routes
}
```

**File:** `app/Models/Ninja.php`
```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Ninja extends Model
{
    protected $fillable = ['name', 'skill', 'bio', 'dojo_id'];

    /** @use HasFactory<\Database\Factories\NinjaFactory> */
    use HasFactory;

    public function dojo()
    {
        return $this->belongsTo(Dojo::class);
    }
}
```

**File:** `resources/views/ninjas/create.blade.php`
```blade
<x-layout>
  <form action="{{ route('ninjas.store') }}" method="POST">
    <!-- CSRF token for security -->
    @csrf

    <h2>Create a New Ninja</h2>

    <!-- ninja Name -->
    <label for="name">Ninja Name:</label>
    <input 
      type="text" 
      id="name" 
      name="name" 
      required
    >

    <!-- ninja Strength -->
    <label for="skill">Ninja Skill (0-100):</label>
    <input 
      type="number" 
      id="skill" 
      name="skill" 
      required
    >

    <!-- ninja Bio -->
    <label for="bio">Biography:</label>
    <textarea
      rows="5"
      id="bio" 
      name="bio" 
      required
    ></textarea>

    <!-- select a dojo -->
    <label for="dojo_id">Dojo:</label>
    <select id="dojo_id" name="dojo_id" required>
      <option value="" disabled selected>Select a dojo</option>
      @foreach ($dojos as $dojo)
        <option value="{{ $dojo->id }}">
          {{ $dojo->name }}
        </option>
      @endforeach
    </select>

    <button type="submit" class="btn mt-4">Create Ninja</button>

    <!-- validation errors -->
    
  </form>
</x-layout>
```

**File:** `routes/web.php`
```php
<?php

use App\Http\Controllers\NinjaController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/ninjas', [NinjaController::class, 'index'])->name('ninjas.index');
Route::get('/ninjas/create', [NinjaController::class, 'create'])->name('ninjas.create');
Route::get('/ninjas/{id}', [NinjaController::class, 'show'])->name('ninjas.show');
Route::post('/ninjas', [NinjaController::class, 'store'])->name('ninjas.store');
```

### Lesson 20 — Laravel Tutorial for Beginners #20 - Showing Form Errors

**File:** `resources/views/ninjas/create.blade.php`
```blade
<x-layout>
  <form action="{{ route('ninjas.store') }}" method="POST">
    <!-- CSRF token for security -->
    @csrf

    <h2>Create a New Ninja</h2>

    <!-- ninja Name -->
    <label for="name">Ninja Name:</label>
    <input 
      type="text" 
      id="name" 
      name="name"
      value="{{ old('name') }}" 
      required
    >

    <!-- ninja Strength -->
    <label for="skill">Ninja Skill (0-100):</label>
    <input 
      type="number" 
      id="skill" 
      name="skill"
      value="{{ old('skill') }}"
      required
    >

    <!-- ninja Bio -->
    <label for="bio">Biography:</label>
    <textarea
      rows="5"
      id="bio" 
      name="bio"
      required
    >{{ old('bio') }}</textarea>

    <!-- select a dojo -->
    <label for="dojo_id">Dojo:</label>
    <select id="dojo_id" name="dojo_id" required>
      <option value="" disabled selected>Select a dojo</option>
      @foreach ($dojos as $dojo)
        <option value="{{ $dojo->id }}" {{ $dojo->id == old('dojo_id') ? 'selected' : '' }}>
          {{ $dojo->name }}
        </option>
      @endforeach
    </select>

    <button type="submit" class="btn mt-4">Create Ninja</button>

    <!-- validation errors -->
    @if ($errors->any())
      <ul class="px-4 py-2 bg-red-100">
        @foreach ($errors->all() as $error)
          <li class="my-2 text-red-500">{{ $error }}</li>
        @endforeach
      </ul>
    @endif
    
  </form>
</x-layout>
```

### Lesson 21 — Laravel Tutorial for Beginners #21 - DELETE Requests

**File:** `app/Http/Controllers/NinjaController.php`
```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Ninja;
use App\Models\Dojo;

class NinjaController extends Controller
{
    public function index() {
      // route --> /ninjas/
      $ninjas = Ninja::with('dojo')->orderBy('created_at', 'desc')->paginate(10);

      return view('ninjas.index', ['ninjas' => $ninjas]);
    }

    public function show($id) {
      // route --> /ninjas/{id}
      $ninja = Ninja::with('dojo')->findOrFail($id);

      return view('ninjas.show', ['ninja' => $ninja]);
    }

    public function create() {
      // route --> /ninjas/create
      $dojos = Dojo::all();

      return view('ninjas.create', ['dojos' => $dojos]);
    }

    public function store(Request $request) {
      // --> /ninjas/ (POST)
      $validated = $request->validate([
        'name' => 'required|string|max:255',
        'skill' => 'required|integer|min:0|max:100',
        'bio' => 'required|string|min:20|max:1000',
        'dojo_id' => 'required|exists:dojos,id',
      ]);

      Ninja::create($validated);

      return redirect()->route('ninjas.index');
    }

    public function destroy($id) {
      // --> /ninjas/{id} (DELETE)
      $ninja = Ninja::findOrFail($id);
      $ninja->delete();

      return redirect()->route('ninjas.index');
    }

    // edit() and update() for edit view and update requests
    // we won't be using these routes
}
```

**File:** `resources/views/ninjas/show.blade.php`
```blade
<x-layout>
  <h2>{{ $ninja->name }}'s Profile</h2>

  {{-- ninja info --}}
  <div class="bg-gray-200 p-4 rounded">
    <p><strong>Skill level:</strong> {{ $ninja->skill }}</p>
    <p><strong>About me:</strong></p>
    <p>{{ $ninja->bio }}</p>
  </div>

  {{-- dojo info --}}
  <div class="border-2 border-dashed bg-white px-4 pb-4 my-4 rounded">
    <h3>Dojo Information</h3>
    <p><strong>Dojo name:</strong> {{ $ninja->dojo->name }}</p>
    <p><strong>Location:</strong> {{ $ninja->dojo->location }}</p>
    <p><strong>About the Dojo:</strong></p>
    <p>{{ $ninja->dojo->description }}</p>
  </div>

  {{-- delete button --}}
  <form action="{{ route('ninjas.destroy', $ninja) }}" method="POST">
    @csrf
    @method('DELETE')

    <button type="submit" class="btn my-4">Delete Ninja</button>
  </form>

</x-layout>
```

**File:** `routes/web.php`
```php
<?php

use App\Http\Controllers\NinjaController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/ninjas', [NinjaController::class, 'index'])->name('ninjas.index');
Route::get('/ninjas/create', [NinjaController::class, 'create'])->name('ninjas.create');
Route::get('/ninjas/{id}', [NinjaController::class, 'show'])->name('ninjas.show');
Route::post('/ninjas', [NinjaController::class, 'store'])->name('ninjas.store');
Route::delete('/ninjas/{ninja}', [NinjaController::class, 'destroy'])->name('ninjas.destroy');
```

### Lesson 22 — Laravel Tutorial for Beginners #22 - Flash Messages

**File:** `app/Http/Controllers/NinjaController.php`
```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Ninja;
use App\Models\Dojo;

class NinjaController extends Controller
{
    public function index() {
      // route --> /ninjas/
      $ninjas = Ninja::with('dojo')->orderBy('created_at', 'desc')->paginate(10);

      return view('ninjas.index', ['ninjas' => $ninjas]);
    }

    public function show($id) {
      // route --> /ninjas/{id}
      $ninja = Ninja::with('dojo')->findOrFail($id);

      return view('ninjas.show', ['ninja' => $ninja]);
    }

    public function create() {
      // route --> /ninjas/create
      $dojos = Dojo::all();

      return view('ninjas.create', ['dojos' => $dojos]);
    }

    public function store(Request $request) {
      // --> /ninjas/ (POST)
      $validated = $request->validate([
        'name' => 'required|string|max:255',
        'skill' => 'required|integer|min:0|max:100',
        'bio' => 'required|string|min:20|max:1000',
        'dojo_id' => 'required|exists:dojos,id',
      ]);

      Ninja::create($validated);

      return redirect()->route('ninjas.index')->with('success', 'Ninja created!');
    }

    public function destroy($id) {
      // --> /ninjas/{id} (DELETE)
      $ninja = Ninja::findOrFail($id);
      $ninja->delete();

      return redirect()->route('ninjas.index')->with('success', 'Ninja deleted!');
    }

    // edit() and update() for edit view and update requests
    // we won't be using these routes
}
```

**File:** `resources/js/app.js`
```javascript
import './bootstrap';
```

**File:** `resources/views/components/layout.blade.php`
```blade
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ninja Network</title>

  @vite('resources/css/app.css')
</head>
<body>
  @if (session('success'))
    <div id="flash" class="p-4 text-center bg-green-50 text-green-500 font-bold">
      {{ session('success') }}
    </div>
  @endif

  <header>
    <nav>
      <h1>Ninja Network</h1>
      <a href="{{ route('ninjas.index') }}"> 
        All Ninjas
      </a>
      <a href="{{ route('ninjas.create') }}">
        Create New Ninja
      </a>
    </nav>
  </header>

  <main class="container">
    {{ $slot }}
  </main>
</body>
</html>
```

### Lesson 23 — Laravel Tutorial for Beginners #23 - Route Model Binding

**File:** `app/Http/Controllers/NinjaController.php`
```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Ninja;
use App\Models\Dojo;

class NinjaController extends Controller
{
    public function index() {
      // route --> /ninjas/
      $ninjas = Ninja::with('dojo')->orderBy('created_at', 'desc')->paginate(10);

      return view('ninjas.index', ['ninjas' => $ninjas]);
    }

    public function show(Ninja $ninja) {
      // route --> /ninjas/{id}
      $ninja->load('dojo');

      return view('ninjas.show', ['ninja' => $ninja]);
    }

    public function create() {
      // route --> /ninjas/create
      $dojos = Dojo::all();

      return view('ninjas.create', ['dojos' => $dojos]);
    }

    public function store(Request $request) {
      // --> /ninjas/ (POST)
      $validated = $request->validate([
        'name' => 'required|string|max:255',
        'skill' => 'required|integer|min:0|max:100',
        'bio' => 'required|string|min:20|max:1000',
        'dojo_id' => 'required|exists:dojos,id',
      ]);

      Ninja::create($validated);

      return redirect()->route('ninjas.index')->with('success', 'Ninja created!');
    }

    public function destroy(Ninja $ninja) {
      // --> /ninjas/{id} (DELETE)
      $ninja->delete();

      return redirect()->route('ninjas.index')->with('success', 'Ninja deleted!');
    }

    // edit() and update() for edit view and update requests
    // we won't be using these routes
}
```

**File:** `resources/views/ninjas/show.blade.php`
```blade
<x-layout>
  <h2>{{ $ninja->name }}'s Profile</h2>

  {{-- ninja info --}}
  <div class="bg-gray-200 p-4 rounded">
    <p><strong>Skill level:</strong> {{ $ninja->skill }}</p>
    <p><strong>About me:</strong></p>
    <p>{{ $ninja->bio }}</p>
  </div>

  {{-- dojo info --}}
  <div class="border-2 border-dashed bg-white px-4 pb-4 my-4 rounded">
    <h3>Dojo Information</h3>
    <p><strong>Dojo name:</strong> {{ $ninja->dojo->name }}</p>
    <p><strong>Location:</strong> {{ $ninja->dojo->location }}</p>
    <p><strong>About the Dojo:</strong></p>
    <p>{{ $ninja->dojo->description }}</p>
  </div>

  {{-- delete button --}}
  <form action="{{ route('ninjas.destroy', $ninja->id) }}" method="POST">
    @csrf
    @method('DELETE')

    <button type="submit" class="btn my-4">Delete Ninja</button>
  </form>

</x-layout>
```

**File:** `routes/web.php`
```php
<?php

use App\Http\Controllers\NinjaController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/ninjas', [NinjaController::class, 'index'])->name('ninjas.index');
Route::get('/ninjas/create', [NinjaController::class, 'create'])->name('ninjas.create');
Route::get('/ninjas/{ninja}', [NinjaController::class, 'show'])->name('ninjas.show');
Route::post('/ninjas', [NinjaController::class, 'store'])->name('ninjas.store');
Route::delete('/ninjas/{ninja}', [NinjaController::class, 'destroy'])->name('ninjas.destroy');
```
